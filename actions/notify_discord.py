# filepath: /opt/stackstorm/packs/monitor_test/actions/notify_discord.py
from st2common.runners.base_action import Action
import requests

class NotifyDiscordAction(Action):
    def run(self, webhook_url, message):
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        return {"status": response.status_code, "response": response.text}