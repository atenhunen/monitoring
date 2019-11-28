"""Test for server emulator."""

from monitoring.server import ping


def test_ping():
    """Server emulator test."""
    ret = ping()
    print(ret)
    correct_options = [
        "{'type': 'error', 'message': 'Internal Server Error'}",
        "{'type': 'success', 'message': 'Fetching users'}",
        "{'type': 'info', 'message': 'User is trying to fetch past 1 year data.'}",
        "{'type': 'debug', 'message': 'Infrastructure at peak load'}"]
    assert ret in correct_options
