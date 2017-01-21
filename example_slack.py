#!/usr/bin/env python
"""Sets a luxafor flag based on status."""

import luxafor
import os
import time
from slackclient import SlackClient


slack_token = os.environ["SLACK_API_TOKEN"]
slack_client = SlackClient(slack_token)
lux = luxafor.API()
snooze_remaining = -1  # Countdown timer
user_id = 'U024G0M2L'

if slack_client.rtm_connect():
    while True:
        try:
            for event in slack_client.rtm_read():
                if event['type'] == 'dnd_updated' and event['user'] == user_id:
                    if event['dnd_status']['snooze_enabled'] is True:
                        lux.mode_colour(luxafor.COLOUR_RED)
                        snooze_remaining = event['dnd_status']['snooze_remaining']
                    else:
                        lux.mode_colour(luxafor.COLOUR_GREEN)
        except KeyError:
            pass

        if snooze_remaining >= 1:
            snooze_remaining -= 1
        if snooze_remaining == 0 or snooze_remaining == -1:
            lux.mode_colour(luxafor.COLOUR_GREEN)
            snooze_remaining = -1

        time.sleep(1)

else:
    print("Connection Failed, invalid token?")
