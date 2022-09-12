import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



def on_modified(event):
    pass


def Data_listener():
    
    event_handler = FileSystemEventHandler()
    event_handler.on_modified=on_modified
    observer = Observer()
    observer.schedule(event_handler, r'D:\Email_campaign_website\app\Data', recursive=True)
    observer.start()
    try:
        print("Monitoring..")
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()