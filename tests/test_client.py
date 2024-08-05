import inspect

from slack_sdk import WebClient

from mlack import MockClient

# We can use a random token; it's a mock client
mock_client = MockClient(token="xoxb-{token}")
assert mock_client is not None


def test_all_methods():
    """A test to ensure that all public methods from the `WebClient` class are in the `MockClient` class"""

    # Get all the methods from the `WebClient` class and the `MockClient` class
    webclient_methods = {name for name, _ in inspect.getmembers(WebClient, predicate=inspect.isfunction)}
    mockclient_methods = {name for name, _ in inspect.getmembers(MockClient, predicate=inspect.isfunction)}
    # Make sure each public method from the `WebClient` class is in the `MockClient` class
    for method_name in mockclient_methods:
        if not method_name.startswith('_'):
            assert method_name in webclient_methods


def test_users_info():
    """Assert that the `users_info` method returns the correct response"""
    response = mock_client.users_info(user="U123456")
    assert response["ok"] is True
    assert response["user"]["id"] == "U123456"


def test_users_conversations():
    """Assert that the `users_conversations` method returns the correct response"""
    response = mock_client.users_conversations()
    assert response["ok"] is True
