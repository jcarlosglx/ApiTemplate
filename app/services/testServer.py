from platform import system as system_platform
from pathlib import Path
from subprocess import Popen
from time import sleep


class TestServer:
    def __init__(self, time_wake_sec: int):
        self.time_wait = time_wake_sec
        self.time_close = time_wake_sec*2
        self.current_path = Path(__file__).absolute().parent.parent.parent
        type_platform = system_platform()

        if type_platform == "Windows":
            self.test_files_path = f'"{self.current_path}\\__test"'
            self.main_files_path = f'"{self.current_path}\\main.py"'
        else:
            self.test_files_path = f'"{self.current_path}/__test"'
            self.main_files_path = f'"{self.current_path}/main.py"'

    def __enter__(self):
        self.server = Popen(["python", f"{self.main_files_path}", "run_server"])
        print(f"Waiting {self.time_wait} for awake server")
        sleep(self.time_wait)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing server test")
        current_time = 0.0
        self.server.kill()
        while (self.server.poll() is None) and (current_time < self.time_close):
            sleep(0.5)
            current_time += 0.5

        if current_time > self.time_close:
            print(f"Unable to close the server test {self.server.pid}")
            return self.server.pid

        print("Closed the server test")
        return self.server.returncode