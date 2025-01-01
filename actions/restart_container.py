from st2common.runners.base_action import Action
import subprocess

class RestartContainerAction(Action):
    def run(self, container_id):
        try:
            # Restart the Docker container
            subprocess.run(["docker", "restart", container_id], check=True)
            return {"status": "success", "message": f"Container {container_id} restarted successfully."}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}