import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from pypresence import Presence


def set_presence(state: str = None):
    presence.update(large_image="logo",
                    large_text="git.io/Jv6NZ",
                    start=begin_time,
                    state=state)


class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file_path = event.src_path
        # Only watch for the Client.txt log file
        if "Client.txt" not in file_path:
            return

        with open(file_path, "r") as f:
            # Read the last line from Client.txt
            line = f.readlines()[-1]

            if "entered" in line:
                # Strip the line to just the location name
                entered_location = \
                    line.split("entered")[1].replace(".", "").strip()

                set_presence(entered_location)
                print(f"Entered {entered_location}")


if __name__ == "__main__":
    path = sys.argv[1]
    if not path:
        print("Log path not given, exitting.")
        exit(1)

    begin_time = time.time()
    presence = Presence("655060628582432768")
    observer = Observer()
    event_handler = FileEventHandler()

    observer.schedule(event_handler, path)
    observer.start()
    print("Started file watcher")

    presence.connect()
    print("Started Discord Presence")
    print("=" * 20, end="\n\n")

    # Default presence
    set_presence("Main Menu")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        presence.close()

    observer.join()
