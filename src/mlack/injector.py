from functools import partial

import httpretty
from typing import Callable, Dict

from .globals import MOCK_AVATAR_URL
from .mock_api import (
    users_info,
    user_conversations,
    conversations_history,
    conversations_replies,
    avatar, post_message,
)
from .mock_responses import MockUserConversations


class EventBus:
    def __init__(self):
        self.listeners = {}
        self.messages = []
        self.channels = MockUserConversations().typical_response["channels"]

    def on(self, event, callback):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)

    def emit(self, event, *args, **kwargs):
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(*args, **kwargs)


event_bus = EventBus()
event_bus.on("message", lambda message: event_bus.messages.append(message))

# Define a custom class for the URIs dictionary
class Endpoint:
    def __init__(self, response: Callable, method: str):
        self.response = response
        self.method = method

# Define the URIs dictionary with type annotations
URIsType = Dict[str, Endpoint]

# Define the URIs dictionary with instances of the Endpoint class
uris: URIsType = {
    "https://slack.com/api/users.info": Endpoint(users_info, "POST"),
    "https://slack.com/api/users.conversations": Endpoint(user_conversations, "POST"),
    "https://slack.com/api/conversations.history": Endpoint(conversations_history, "POST"),
    "https://slack.com/api/conversations.replies": Endpoint(conversations_replies, "POST"),
    MOCK_AVATAR_URL: Endpoint(avatar, "GET"),
    "https://slack.com/api/chat.postMessage": Endpoint(post_message, "POST"),
}

def inject():
    httpretty.enable(verbose=True, allow_net_connect=True)
    for uri, endpoint in uris.items():
        httpretty.register_uri(endpoint.method, uri, body=partial(endpoint.response, event_bus=event_bus))