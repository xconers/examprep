# === Stage 61: Add performance timing for core list and search operations ===
# Project: ExamPrep
import time

def _timeit(func, samples=5):
    results = []
    for _ in range(samples):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        results.append(end - start)
    return min(results)

def time_list_append(lst, n):
    def _run():
        for i in range(n):
            lst.append(i)
    return _timeit(_run)

def time_list_index(lst, target):
    def _run():
        return lst.index(target)
    return _timeit(_run)

def time_list_contains(lst, target):
    def _run():
        return target in lst
    return _timeit(_run)

def time_list_search(lst, target):
    def _run():
        for i, item in enumerate(lst):
            if item == target:
                return i
        return -1
    return _timeit(_run)

def time_list_remove(lst, target):
    def _run():
        lst.remove(target)
    return _timeit(_run)

def time_list_sort(lst):
    def _run():
        arr = list(lst)
        arr.sort()
        return arr
    return _timeit(_run)

def time_linear_search(arr, target):
    def _run():
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    return _timeit(_run)

def time_binary_search(arr, target):
    def _run():
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
    return _timeit(_run)
