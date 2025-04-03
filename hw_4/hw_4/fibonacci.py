from multiprocessing import Process
from threading import Thread


class Fibonacci:
    def __init__(self, n, fib_number):
        self._n = n
        self._fib_number = fib_number

    def sync_execute(self):
        for _ in range(self._n):
            self._nth_fibonaci(self._fib_number)

    def execute_thread(self):
        self._execute(executor_fn=Thread, target_fn=self._nth_fibonaci, args=(self._fib_number,))

    def execute_process(self):
        self._execute(executor_fn=Process, target_fn=self._nth_fibonaci, args=(self._fib_number,))

    def _execute(self, executor_fn, target_fn, args):
        executors = [executor_fn(target=target_fn, args=args) for _ in range(self._n)]
        for executor in executors:
            executor.start()
        for executor in executors:
            executor.join()

    def _nth_fibonaci(self, n: int):
        if n < 2:
            return n
        return self._nth_fibonaci(n - 1) + self._nth_fibonaci(n - 2)


__all__ = [
    'Fibonacci'
]
