from st2common.runners.base_action import Action
import os
import shutil

class CleanCacheAction(Action):
    def run(self):
        # Logic to clean cache goes here
        cache_dirs = [
            "/path/to/cache/dir1",
            "/path/to/cache/dir2"
        ]

        for cache_dir in cache_dirs:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
                os.makedirs(cache_dir)

        return {"status": "Cache cleaned successfully"}