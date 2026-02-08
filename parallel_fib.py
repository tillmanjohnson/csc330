import os
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    values = [35,36,37,38,39]
    children = []
    start = time.perf_counter()

    for n in values:
        pid = os.fork()
        if pid == 0:
            result = fib(n)
            print(f"fib({n}) = {result}")
            os._exit(0)
        else:
            children.append(pid)
    for _ in children:
        os.wait()

    end = time.perf_counter()
    total = end - start
    print(f"Total elapsed time: {total} seconds")

if __name__ == "__main__":
    main()
