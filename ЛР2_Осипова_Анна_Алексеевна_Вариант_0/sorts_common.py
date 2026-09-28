import random, statistics, time

def generate_data(n, lo=0, hi=100_000, seed=42):
    rng = random.Random(seed + n)
    return [rng.randint(lo, hi) for _ in range(n)]

def measure(sort_func, data, repeats=3):
    expected = sorted(data)
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = sort_func(data)
        times.append(time.perf_counter() - start)
        assert result == expected
    return statistics.median(times)
