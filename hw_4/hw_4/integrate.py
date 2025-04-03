import time
from concurrent.futures import wait


def integrate(f, a, b, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def parallel_processing(f, a, b, n_jobs, n_iter, executor):
    chunk_size = (b - a) / n_jobs
    threads_num = min(n_jobs, n_iter)

    offset = a
    chunks = []

    for i in range(threads_num):
        chunks.append((offset, offset + chunk_size))
        offset += chunk_size

    futures = []

    before = time.time()
    for chunk in chunks:
        futures.append(executor.submit(
            integrate,
            f,
            chunk[0],
            chunk[1],
            max(n_iter // n_jobs, 1)
        ))

    wait(futures)

    res = 0
    for future in futures:
        res += future.result()

    return time.time() - before, res


__all__ = [
    'parallel_processing',
    'integrate'
]
