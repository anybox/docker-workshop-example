import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

COUNTER_PATH = os.getenv('COUNTER_PATH', '/tmp/counter.txt')


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            with open(COUNTER_PATH) as f:
                print('%s' % f.read(), end="\r")


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(COUNTER_PATH))
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
