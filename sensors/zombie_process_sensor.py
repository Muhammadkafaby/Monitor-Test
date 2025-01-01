import psutil
from st2reactor.sensor.base import PollingSensor

class ZombieProcessSensor(PollingSensor):
    def __init__(self, sensor_service, config=None):
        super(ZombieProcessSensor, self).__init__(sensor_service, config)
        self._poll_interval = self.config.get('poll_interval', 10)

    def poll(self):
        zombie_processes = [p for p in psutil.process_iter(['pid', 'name', 'status']) if p.info['status'] == 'zombie']
        for process in zombie_processes:
            self.logger.info(f"Zombie process detected: {process.info}")
            self.dispatch(trigger='monitor_test.zombie_detected', payload=process.info)