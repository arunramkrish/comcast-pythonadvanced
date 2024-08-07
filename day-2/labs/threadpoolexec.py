from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Starting task {name}")
    time.sleep(2)
    print(f"Task {name} completed")
    return "Done " + str(name)

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=1000) as executor:
    futures = [executor.submit(task, i) for i in range(2000)]

    for i in range(0,5):
        print("in " + str(i))
        print(futures[5 - i - 1].result())
