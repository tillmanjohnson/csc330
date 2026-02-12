import time 
from multiprocessing import Process

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def comp_fib(n):
    result = fib(n)
    print(f"fib({n}) = {result}")

if __name__ == "__main__":
    values = [35,36,37,38,39]
    processes = []
    start = time.perf_counter()

    for i in values:
        p = Process(target=comp_fib, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.perf_counter()
    total = end - start

    print(f"Total time: {total} Seconds")
