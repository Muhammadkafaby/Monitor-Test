# filepath: /opt/stackstorm/packs/monitor_test/actions/advanced_monitoring.py
from st2common.runners.base_action import Action
import time
import requests
import yaml

class AdvancedMonitoringAction(Action):
    def run(self, config_path):
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)

        webhook_url = config['webhook_url']
        poll_interval = config['poll_interval']
        cpu_threshold = config['cpu_threshold']
        memory_threshold = config['memory_threshold']
        disk_threshold = config['disk_threshold']

        while True:
            # Simulate monitoring logic
            cpu_usage = 85  # Replace with actual CPU usage fetching logic
            memory_usage = 80  # Replace with actual memory usage fetching logic
            disk_usage = 75  # Replace with actual disk usage fetching logic

            if cpu_usage > cpu_threshold or memory_usage > memory_threshold or disk_usage > disk_threshold:
                message = f"Alert! CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%"
                requests.post(webhook_url, json={"content": message})

            time.sleep(poll_interval)