from pathlib import Path
import csv, platform, sys
import matplotlib.pyplot as plt
from sorts_common import generate_data, measure

SIZES = [500, 1000, 2000, 3000, 4000, 5000]
REPEATS = 3

def bubble_sort(arr):
    a = arr.copy()
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def main():
    algs = {"Пузырьком": bubble_sort, "Вставками": insertion_sort}
    results = {name: [] for name in algs}
    for n in SIZES:
        data = generate_data(n)
        for name, func in algs.items():
            results[name].append(measure(func, data, REPEATS))

    with open("results.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["n", "bubble_s", "insertion_s", "bubble_T/n2", "insertion_T/n2"])
        for i, n in enumerate(SIZES):
            b, ins = results["Пузырьком"][i], results["Вставками"][i]
            w.writerow([n, f"{b:.8f}", f"{ins:.8f}", f"{b/n**2:.12e}", f"{ins/n**2:.12e}"])

    plt.figure(figsize=(9, 5.5))
    plt.plot(SIZES, results["Пузырьком"], marker="o", label="Пузырьком")
    plt.plot(SIZES, results["Вставками"], marker="o", label="Вставками")
    plt.xlabel("Размер массива n"); plt.ylabel("Медианное время, с")
    plt.title("ЛР №2, вариант 0"); plt.grid(True); plt.legend(); plt.tight_layout()
    plt.savefig("lr2_plot.png", dpi=160); plt.close()

    lines = ["ЛР №2, вариант 0 — Осипова Анна Алексеевна",
             f"Python: {sys.version.split()[0]}",
             f"ОС: {platform.system()} {platform.release()}",
             f"Процессор: {platform.processor() or 'не определён'}", ""]
    prev = None
    for i, n in enumerate(SIZES):
        b, ins = results["Пузырьком"][i], results["Вставками"][i]
        ratio = "-" if prev is None else f"bubble={b/prev[0]:.3f}, insertion={ins/prev[1]:.3f}"
        lines.append(f"n={n}: bubble={b:.8f} c; insertion={ins:.8f} c; T(2n)/T(n)={ratio}")
        prev = (b, ins)
    Path("results.txt").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
