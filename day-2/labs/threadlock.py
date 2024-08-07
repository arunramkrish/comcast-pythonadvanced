import threading
import time

lock = threading.Lock()
rlock = threading.RLock()

def safe_print(counter):
    with rlock:
        with lock:
            print("Thread-safe print")
            time.sleep(2)
            print("Thread-safe print2")
            print("Thread-safe print3")

# Create threads
threads = [threading.Thread(target=safe_print) for _ in range(5)]

# Start threads
for thread in threads:
    thread.start()

# Wait for threads to complete
for thread in threads:
    thread.join()
