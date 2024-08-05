# Mlack
A Python libary that wraps around the Slack API and makes it easy to test your Slack bot.

## Installation
(Not yet available, still in development)
```bash
pip install mlack
```

## Usage
```python
from mlack import MockClient
# Initialize the MockClient as normal
client = MockClient(token="xoxb-{}")

# Use the client as you would normally

# Example: Get the history of a channel
client.conversations_history(channel="C1234567890")

# Example: Get the replies to a thread
client.conversations_replies(channel="C1234567890", ts="1234567890.123456")

```

**PS**: This is still in development, so not all methods are available yet. If you want to contribute, feel free to open a PR.
