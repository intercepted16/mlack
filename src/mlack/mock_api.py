from .mock_responses import MockUser, MockUserConversations, MockConversationsHistory, MockConversationsReplies
import json


def users_info(request, uri, response_headers):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        print(request.body)
        # weird quirk with the request body, it's a string
        body = request.body.decode("utf-8")
        user = body.split("=")[1]
        return [200, response_headers, json.dumps(MockUser(user).typical_response)]


def user_conversations(request, uri, response_headers):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        return [
            200,
            response_headers,
            json.dumps(MockUserConversations().typical_response),
        ]


def conversations_history(request, uri, response_headers):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        return [
            200,
            response_headers,
            json.dumps(MockConversationsHistory().typical_response),
        ]


def conversations_replies(request, uri, response_headers):
    if not request.headers.get("Authorization"):
        return [200, response_headers, json.dumps({"ok": False, "error": "not_authed"})]
    else:
        return [
            200,
            response_headers,
            json.dumps(MockConversationsReplies().typical_response),
        ]
