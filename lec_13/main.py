import threading
import multiprocessing
import time
from collections import defaultdict

def count_words_sequential(filename):
    word_counts = defaultdict(int)
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                word_counts[word] += 1
    return word_counts


def count_words_in_chunk(chunk, word_counts, lock=None):
    local_counts = defaultdict(int)
    for line in chunk:
        words = line.split()
        for word in words:
            word = word.lower()
            local_counts[word] += 1

    if lock:
        with lock:
            for word, count in local_counts.items():
                word_counts[word] += count
    else:
        return local_counts


def count_words_multithreaded(filename, num_threads=4):
    word_counts = defaultdict(int)
    lock = threading.Lock()

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        chunk = lines[start_index:end_index]

        thread = threading.Thread(target=count_words_in_chunk, args=(chunk, word_counts, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_counts



def count_words_multiprocessing(filename, num_processes=4):
    manager = multiprocessing.Manager()
    word_counts = manager.dict()

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_processes
    processes = []

    for i in range(num_processes):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_processes - 1 else len(lines)
        chunk = lines[start_index:end_index]

        process = multiprocessing.Process(target=count_words_in_chunk, args=(chunk, word_counts))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return dict(word_counts)


def measure_execution_time(func, filename, *args):
    start_time = time.time()
    func(filename, *args)
    end_time = time.time()
    return end_time - start_time



if __name__ == "__main__":
    filename = "file.txt"

    sequential_time = measure_execution_time(count_words_sequential, filename)
    print(f"Sequential execution time: {sequential_time:.4f} seconds")


    num_threads = 4
    multithreading_time = measure_execution_time(count_words_multithreaded, filename, num_threads)
    print(f"Multithreading execution time with {num_threads} threads: {multithreading_time} seconds")

    num_processes = 4
    multiprocessing_time = measure_execution_time(count_words_multiprocessing, filename, num_processes)
    print(f"Multiprocessing execution time with {num_processes} processes: {multiprocessing_time} seconds")


    speedup_threading = sequential_time / multithreading_time
    speedup_multiprocessing = sequential_time / multiprocessing_time

    print(f"Speedup (Multithreading): {speedup_threading}")
    print(f"Speedup (Multiprocessing): {speedup_multiprocessing}")
