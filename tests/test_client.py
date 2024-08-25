import inspect

from slack_sdk import WebClient

from mlack import MockClient
from mlack.mock_responses import MockUserConversations

# We can use a random token; it's a mock client
mock_client = MockClient(token="xoxb-{token}")
assert mock_client is not None


def test_all_methods():
    """A test to ensure that all public methods from the `WebClient` class are in the `MockClient` class"""

    # Get all the methods from the `WebClient` class and the `MockClient` class
    webclient_methods = {
        name for name, _ in inspect.getmembers(WebClient, predicate=inspect.isfunction)
    }
    mockclient_methods = {
        name for name, _ in inspect.getmembers(MockClient, predicate=inspect.isfunction)
    }
    # Make sure each public method from the `WebClient` class is in the `MockClient` class, excluding 'get'
    for method_name in mockclient_methods:
        if not method_name.startswith("_") and method_name != "get":
            assert method_name in webclient_methods


def test_users_info():
    """Assert that the `users_info` method returns the correct response"""
    response = mock_client.users_info(user="U123456")
    assert response["ok"] is True
    assert response["user"]["id"] == "U123456"


def test_avatar():
    """Assert that the image returned from a user can be retrieved"""
    response = mock_client.users_info(user="U123456")
    assert response["ok"] is True
    user = response["user"]
    assert user["profile"]["image_48"] is not None
    # try fetching the image (but using the mocked client, so it has injected responses)
    res = mock_client.get(user["profile"]["image_48"])
    assert res.status_code == 200
    assert res.content is not None


def test_post_message():
    test_channel = MockUserConversations().typical_response["channels"][0]["id"]
    print("Test channel is", test_channel)
    """Assert that the `post_message` method returns the correct response"""
    response = mock_client.chat_postMessage(channel=test_channel, text="Hello!")
    assert response["ok"] is True
    """Assert that the message was sent to the correct channel and is the correct message"""
    history = mock_client.conversations_history(channel=test_channel)
    assert history["ok"] is True
    assert len(history["messages"]) == 1
    assert history["messages"][0]["text"] == "Hello!"
