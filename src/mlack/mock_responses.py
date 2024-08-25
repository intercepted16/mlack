import names

from mlack.globals import MOCK_AVATAR_URL


class MockUserConversations:
    def __init__(self):
        self.typical_response = {
            "ok": True,
            "channels": [
                {
                    "id": "C012AB3CD",
                    "name": "general",
                    "is_channel": True,
                    "is_group": False,
                    "is_im": False,
                    "created": 1449252889,
                    "creator": "U012A3CDE",
                    "is_archived": False,
                    "is_general": True,
                    "unlinked": 0,
                    "name_normalized": "general",
                    "is_shared": False,
                    "is_ext_shared": False,
                    "is_org_shared": False,
                    "pending_shared": [],
                    "is_pending_ext_shared": False,
                    "is_member": True,
                    "is_private": False,
                    "is_mpim": False,
                    "updated": 1678229664302,
                    "topic": {
                        "value": "Company-wide announcements and work-based matters",
                        "creator": "",
                        "last_set": 0,
                    },
                    "purpose": {
                        "value": "This channel is for team-wide communication and announcements. All team members are in this channel.",
                        "creator": "",
                        "last_set": 0,
                    },
                    "previous_names": [],
                },
                {
                    "id": "C061EG9T2",
                    "name": "random",
                    "is_channel": True,
                    "is_group": False,
                    "is_im": False,
                    "created": 1449252889,
                    "creator": "U061F7AUR",
                    "is_archived": False,
                    "is_general": False,
                    "unlinked": 0,
                    "name_normalized": "random",
                    "is_shared": False,
                    "is_ext_shared": False,
                    "is_org_shared": False,
                    "pending_shared": [],
                    "is_pending_ext_shared": False,
                    "is_private": False,
                    "is_mpim": False,
                    "updated": 1678229664302,
                    "topic": {
                        "value": "Non-work banter and water cooler conversation",
                        "creator": "",
                        "last_set": 0,
                    },
                    "purpose": {
                        "value": "A place for non-work-related flimflam, faffing, hodge-podge or jibber-jabber you'd "
                        "prefer to keep out of more focused work-related channels.",
                        "creator": "",
                        "last_set": 0,
                    },
                    "previous_names": [],
                    "num_members": 4,
                },
            ],
            "response_metadata": {"next_cursor": "dGVhbTpDMDYxRkE1UEI="},
        }


class MockConversationsReplies:
    def __init__(self):
        self.typical_response = {
            "ok": True,
            "messages": [
                {
                    "type": "message",
                    "user": "U123ABC456",
                    "text": "Hello!",
                    "ts": "1512085950.000216",
                    "parent_user_id": "U456XYZ789",
                },
            ],
        }


class MockUser:
    def __init__(self, user_id):
        random_full_name = names.get_full_name()
        random_name = names.get_first_name()
        self.typical_response = {
            "ok": True,
            "user": {
                "id": user_id,
                "team_id": "T012AB3C4",
                "name": random_name,
                "deleted": False,
                "color": "9f69e7",
                "real_name": random_full_name,
                "tz": "America/Los_Angeles",
                "tz_label": "Pacific Daylight Time",
                "tz_offset": -25200,
                "profile": {
                    "avatar_hash": "ge3b51ca72de",
                    "status_text": "Print is dead",
                    "status_emoji": ":books:",
                    "real_name": random_full_name,
                    "display_name": random_name,
                    "real_name_normalized": random_full_name,
                    "display_name_normalized": random_name,
                    "email": "spengler@ghostbusters.example.com",
                    "image_original": MOCK_AVATAR_URL,
                    "image_24": MOCK_AVATAR_URL,
                    "image_32": MOCK_AVATAR_URL,
                    "image_48": MOCK_AVATAR_URL,
                    "image_72": MOCK_AVATAR_URL,
                    "image_192": MOCK_AVATAR_URL,
                    "image_512": MOCK_AVATAR_URL,
                    "team": "T012AB3C4",
                },
                "is_admin": True,
                "is_owner": False,
                "is_primary_owner": False,
                "is_restricted": False,
                "is_ultra_restricted": False,
                "is_bot": False,
                "updated": 1502138686,
                "is_app_user": False,
                "has_2fa": False,
            },
        }
