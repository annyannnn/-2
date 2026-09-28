"""Общие функции для лабораторной работы № 2."""
import random
import statistics
import time


def generate_data(n, kind="duplicates", lo=0, hi=10, seed=42):
    """Генерирует воспроизводимый массив заданного типа."""
    rng = random.Random(seed + n)
    data = [rng.randint(lo, hi) for _ in range(n)]
    if kind == "sorted":
        data.sort()
    elif kind == "reversed":
        data.sort(reverse=True)
    elif kind == "nearly_sorted":
        data.sort()
        for _ in range(max(1, n // 20)):
            i, j = rng.randrange(n), rng.randrange(n)
            data[i], data[j] = data[j], data[i]
    return data


def measure(sort_func, data, repeats=3):
    """Возвращает медианное время работы sort_func на копиях data, с."""
    times = []
    expected = sorted(data)
    for _ in range(repeats):
        start = time.perf_counter()
        result = sort_func(data)
        elapsed = time.perf_counter() - start
        times.append(elapsed)
        assert result == expected, f"{sort_func.__name__}: ошибка сортировки"
    return statistics.median(times)
