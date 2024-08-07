import threading

class Product:
    # member variable product_name
    # override the string representation of the object by displayed "Product:{name}

class Warehouse:
    # member max_capacity, collection of products - add, fetch

class Producer:
    # produce method, creates product and adds it to warehouse

class Consumer:
    #consume method, fetch product from warehouse and print it

class Factory:
    # can create threads for producing and consuming
    # start the factory, all threads have to be started

# main method to create and start the factory and stop it after 10 seconds and print how many products are produced in the factory since its started


condition = threading.Condition()

def consumer():
    with condition:
        condition.wait()
        print("Consumer notified")

def producer():
    with condition:
        print("Producer notifying")
        condition.notify_all()

# Create threads
consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

# Start threads
consumer_thread.start()
producer_thread.start()

# Wait for threads to complete
consumer_thread.join()
producer_thread.join()
