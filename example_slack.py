#!/usr/bin/env python
"""Sets a luxafor flag based on status."""

import luxafor
import os
import time
from slackclient import SlackClient


slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

API = luxafor.API()

while (True):
    presence = sc.api_call("dnd.info")

    if presence['snooze_enabled']:
        API.mode_colour(luxafor.COLOUR_RED)
    else:
        API.mode_colour(luxafor.COLOUR_GREEN)

    time.sleep(1)  # make sure we don't flood slack
