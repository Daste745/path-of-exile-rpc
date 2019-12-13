import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pypresence import Presence

RPC = Presence("655060628582432768")

def update_presence(*, state: str = None, details: str = None):
    RPC.update(large_image="logo",
               small_image="rem-padoru",
               large_text="Conquerors of the Atlas",
               small_text="Rich Presence by @Predator#4682",
               start=begin_time,
               state=state)

class CustomFileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file_path = event.src_path
        # Only watch for the Client.txt log file
        if "Client.txt" not in file_path:
            return
        
        with open(file_path, "r") as f:
            line = f.readlines()[-1]

            if "Connected to" in line:
                connected_server = line.split("Connected to")[1].strip().split(" ")[0]
                connected_time = line.split("Connected to")[-1].strip().split(" ")[-1].replace("ms.", "")
                print(f"Connected to server {connected_server} in {connected_time}ms.")
                
                update_presence(state="Idling")


            if "You have entered" in line:
                entered_location = line.split("You have entered")[1].strip().replace(".", "")
                print(f"Entering {entered_location}.")

                update_presence(state=entered_location)
            
path = sys.argv[1]
event_handler = CustomFileEventHandler()
observer = Observer()

if __name__ == "__main__":
    begin_time = time.time()

    observer.schedule(event_handler, path)
    observer.start()
    print("Started watcher")

    RPC.connect()
    print("Started presence")

    # Default presence
    update_presence(state="Idling")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        RPC.close()

    observer.join()
