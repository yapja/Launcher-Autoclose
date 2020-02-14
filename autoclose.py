import psutil
import json
import time
import subprocess
from subprocess import CREATE_NO_WINDOW

with open('processes.json', 'r') as from_file:
    data = from_file.read()
processes = json.loads(data)

while True:
    existing_process = [process.name() for process in psutil.process_iter()]
    for launcher in processes:
        for game in processes[launcher]:
            if (game['game'] in existing_process):
                while True:
                    time.sleep(30)
                    existing_process = [process.name() for process in psutil.process_iter()]
                    same_launcher = False
                    for game in processes[launcher]:
                        if game['game'] in existing_process:
                            same_launcher = True
                    if same_launcher is False:
                        time.sleep(30)
                        CREATE_NO_WINDOW = 0x08000000
                        subprocess.call("taskkill /f /im " + launcher, creationflags = CREATE_NO_WINDOW)
                        break
