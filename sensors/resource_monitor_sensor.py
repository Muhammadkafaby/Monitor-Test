import psutil
from st2reactor.sensor.base import PollingSensor

class ResourceMonitorSensor(PollingSensor):
    def __init__(self, sensor_service, config=None):
        super(ResourceMonitorSensor, self).__init__(sensor_service, config)
        self._poll_interval = self.config.get('poll_interval', 10)

    def poll(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        if cpu_usage > self.config.get('cpu_threshold', 90):
            self.sensor_service.dispatch(trigger='monitor_test.critical_alert', payload={
                'resource': 'cpu',
                'usage': cpu_usage
            })

        if memory.percent > self.config.get('memory_threshold', 90):
            self.sensor_service.dispatch(trigger='monitor_test.critical_alert', payload={
                'resource': 'memory',
                'usage': memory.percent
            })

        if disk.percent > self.config.get('disk_threshold', 90):
            self.sensor_service.dispatch(trigger='monitor_test.critical_alert', payload={
                'resource': 'disk',
                'usage': disk.percent
            })

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass