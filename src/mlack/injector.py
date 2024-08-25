import httpretty

from .globals import MOCK_AVATAR_URL
from .mock_api import (
    users_info,
    user_conversations,
    conversations_history,
    conversations_replies,
    avatar,
)


def inject():
    httpretty.enable(
        verbose=True, allow_net_connect=True
    )  # enable HTTPretty so that it will monkey patch the socket module
    httpretty.register_uri(
        httpretty.POST, "https://slack.com/api/users.info", body=users_info
    )
    httpretty.register_uri(
        httpretty.POST,
        "https://slack.com/api/users.conversations",
        body=user_conversations,
    )
    httpretty.register_uri(
        httpretty.POST,
        "https://slack.com/api/conversations.history",
        body=conversations_history,
    )
    httpretty.register_uri(
        httpretty.POST,
        "https://slack.com/api/conversations.replies",
        body=conversations_replies,
    )
    httpretty.register_uri(httpretty.GET, MOCK_AVATAR_URL, body=avatar)
