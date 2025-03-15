import multiprocessing
from multiprocessing.sharedctypes import Synchronized
from multiprocessing.synchronize import Lock
from decimal import Decimal


def deposit(balance: Synchronized, lock: Lock):
    for v in range(100):
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance: Synchronized, lock: Lock):
    for v in range(100):
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value("i", 200)
    lock = multiprocessing.Lock()
    depositor = multiprocessing.Process(target=deposit, args=[balance, lock])
    withdrawer = multiprocessing.Process(target=withdraw, args=[balance, lock])
    print(f"Starting balance: {balance.value}")

    depositor.start()
    withdrawer.start()
    depositor.join()
    withdrawer.join()

    print(f"Balance after processing: {balance.value}")
