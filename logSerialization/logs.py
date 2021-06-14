import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG)


def thread1(num):
    """
    function to print cube of given num
    """
    if num:
        for i in range(num):
            time.sleep(1)
            logging.info(f"Thread 1: My number is {i}")


def thread2(num):
    """
    function to print square of given num
    """
    if num:
        for i in range(num):
            time.sleep(2)
            logging.info(f"Thread 2: My number is {i}{i}{i}")


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=thread1, args=(5,))
    t2 = threading.Thread(target=thread2, args=(6,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    logging.info("Done!")

