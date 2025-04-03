from hw_4.fibonacci import Fibonacci
from hw_4.integrate import parallel_processing
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math


def count_delta_time(fn):
    start = time.time()
    fn()
    return time.time() - start


if __name__ == "__main__":
    # 4.1
    f = Fibonacci(10, 34)
    with open("./artifacts/4.1.txt", "w") as file:
        file.write('\n'.join([
            "sync: %.2f" % count_delta_time(f.sync_execute),
            "threads: %.2f" % count_delta_time(f.execute_thread),
            "pools: %.2f" % count_delta_time(f.execute_process)
        ]))
    # 4.2
    with open("./artifacts/4.2.txt", "w") as file:
        for n_jobs in range(1, multiprocessing.cpu_count() * 2):
            threads_time, res1 = parallel_processing(
                math.cos, 0, math.pi / 2, n_jobs, 10000000, ThreadPoolExecutor()
            )

            proc_time, res2 = parallel_processing(
                math.cos, 0, math.pi / 2, n_jobs, 10000000, ProcessPoolExecutor()
            )
            file.write('\n'.join([
                "n_jobs: %i" % n_jobs,
                "threads time: %.2f" % threads_time,
                "threads res: %.2f" % res1,
                "procs time: %.2f" % proc_time,
                "procs res: %.2f" % res2,
            ]) + '\n')
