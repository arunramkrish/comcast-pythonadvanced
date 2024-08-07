import multiprocessing
import time

def print_numbers():
    for i in range(5):
        for i in range(1,10000000):
            pass
        # print(i)
        # time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    # Create processes
    process1 = multiprocessing.Process(target=print_numbers)
    # time.sleep(5)
    process2 = multiprocessing.Process(target=print_letters)

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to complete
    process1.join()
    process2.join()
