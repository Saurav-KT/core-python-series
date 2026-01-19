import threading


class FileLock:
    def __init__(self):
        self.lock= threading.Lock()

    def __enter__(self):
        print("Acquiring lock")
        self.lock.acquire()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing lock")
        self.lock.release()

with FileLock():
    print("Critical section")