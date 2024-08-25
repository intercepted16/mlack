# src/mlack/errors/__init__.py

auth_errors = [
    "access_denied",
    "account_inactive",
    "invalid_auth",
    "missing_scope",
    "not_allowed_token_type",
    "not_authed",
    "token_expired",
    "token_revoked",
    "two_factor_setup_required",
    "org_login_required",
]

message_errors = [
    "as_user_not_supported",
    "duplicate_message_not_found",
    "invalid_blocks",
    "invalid_blocks_format",
    "invalid_metadata_format",
    "invalid_metadata_schema",
    "message_limit_exceeded",
    "metadata_must_be_sent_from_app",
    "metadata_too_large",
    "msg_blocks_too_long",
    "msg_too_long",
    "no_text",
    "rate_limited",
    "restricted_action",
    "restricted_action_non_threadable_channel",
    "restricted_action_read_only_channel",
    "restricted_action_thread_locked",
    "restricted_action_thread_only_channel",
    "too_many_attachments",
    "too_many_contact_cards",
    "cannot_reply_to_message",
    "missing_file_data",
    "attachment_payload_limit_exceeded",
]

channel_errors = [
    "channel_not_found",
    "duplicate_channel_not_found",
    "is_archived",
    "not_in_channel",
    "team_access_not_granted",
    "team_not_found",
]

slack_connect_errors = [
    "slack_connect_canvas_sharing_blocked",
    "slack_connect_file_link_sharing_blocked",
    "slack_connect_lists_sharing_blocked",
]

general_errors = {
    "deprecated_endpoint": check_fo,
    "enterprise_is_restricted",
    "fatal_error",
    "internal_error",
    "invalid_arg_name",
    "invalid_arguments",
    "invalid_array_arg",
    "invalid_charset",
    "invalid_form_data",
    "invalid_post_type",
    "missing_post_type",
    "ratelimited",
    "request_timeout",
    "service_unavailable",
    "team_added_to_org",
    "accesslimited",
}

all_errors = auth_errors + message_errors + channel_errors + slack_connect_errors + general_errors


class TypeCouldNotBeFoundError(Exception):
    """Exception raised when the type of a Slack object could not be determined."""

    def __init__(self, message="Type could not be found for the given Slack object."):
        self.message = message
        super().__init__(self.message)


def infer_type(request: dict) -> str:
    """
    Takes a request with an authorization header and an object or an array of objects,
    likely a message, user, or channel object (from the mock Slack API)
    and returns whichever type of Slack object it is.
    Args:
        request (dict): A request object with either: a message, channel or user object.
    Returns:
        type (string): A string representing the type of object, i.e: "message", "channel" or "user".
    Raises:
        TypeCouldNotBeFoundError: An error occured detecting the type of the Slack API object; it is likely invalid.
    """
    if request.get("messages"): return "messages"
    if request.get("channels"): return "channels"
    if request.get("user"): return "user"
    # could not be found, raise exception
    raise TypeCouldNotBeFoundError()


def check_for_errors(request: dict) -> str:
    """
    Given a request with Authorization headers and an object or arrary of objects,
    returned from the Slack API in a JSON format, infer the type of object,
    i.e: a message, a channel, a user.
    Then, check each and every error that could be given for that type.
    Returns the first error found, or None if no error is found.

    Args:
        request (dict): The request object, containing the Authorization headers and an object or array of objects
    Returns:
        str: The first error found in the object, or None if no error is found
    """
    obj_type = infer_type(request)
