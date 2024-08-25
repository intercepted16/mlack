from typing import Dict, List, Any

"""
'Message' is the type of a message object.
A string key is mapped to a dictionary value.
"""
Message = Dict[str, str]
"""
'Channel' is the type of a channel object.
A string key is mapped to a dictionary value.
"""
Channel = Dict[str, Any]
"""
'Messages' is a list of message objects.
"""
Messages = List[Message]

"""
'Channels' is a list of channel objects.
"""
Channels = List[Channel]
