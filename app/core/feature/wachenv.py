import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def track_and_restart_uvicorn_on_env_change(env_file_path, uvicorn_script):
    class EnvFileHandler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.src_path == env_file_path:
                print(f"Файл .env был изменен. Перезапуск Uvicorn...")
                subprocess.Popen(['python', uvicorn_script])

    event_handler = EnvFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()