import os.path
from datetime import datetime, timezone


from .mock_responses import (
    MockUser,
    MockUserConversations,
    MockConversationsReplies,
)
import json


def users_info(request, uri, response_headers, event_bus):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        print(request.body)
        # weird quirk with the request body, it's a string
        body = request.body.decode("utf-8")
        user = body.split("=")[1]
        return [200, response_headers, json.dumps(MockUser(user).typical_response)]


def user_conversations(request, uri, response_headers, event_bus):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        return [
            200,
            response_headers,
            json.dumps(MockUserConversations().typical_response),
        ]


def conversations_history(request, uri, response_headers, event_bus):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        return [
            200,
            response_headers,
            json.dumps({"ok": True, "messages": event_bus.messages}),
        ]


def conversations_replies(request, uri, response_headers, event_bus):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        return [
            200,
            response_headers,
            json.dumps(MockConversationsReplies().typical_response),
        ]


def avatar(_request, _uri, response_headers, event_bus):
    # read the local png and return it
    png_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "assets", "slack.png")
    )
    with open(png_path, "rb") as f:
        return [200, response_headers, f.read()]

def handle_post_message_errors(request, uri, response_headers, event_bus):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    body = json.loads(request.body)
    channel = body.get("channel")
    print(event_bus.channels)
    if channel not in [c["id"] for c in event_bus.channels]:
        return [200, response_headers, json.dumps({"ok": False, "error": "channel_not_found"})]
    else:
        return None


def post_message(request, uri, response_headers, event_bus):
    error = handle_post_message_errors(request, uri, response_headers, event_bus)
    if error:
        return error
    body = json.loads(request.body)
    # get unix timestamp now
    ts = datetime.now(timezone.utc).timestamp()
    body["ts"] = ts
    event_bus.emit("message", body)
    return [200, response_headers, json.dumps({"ok": True})]
