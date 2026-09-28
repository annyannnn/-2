"""
Лабораторная работа № 2.
Осипова Анна Алексеевна, вариант 17.

Эмпирический анализ временной сложности:
сортировка пузырьком и сортировка вставками.

Вариант 17:
n = 1000, 2000, 3000, 4000, 5000
тип данных: D — большое число повторов
диапазон: [0; 10]
повторов: 3
дополнительное задание М7:
сортировка записей (фамилия клиента, сумма заказа) по сумме заказа
с демонстрацией устойчивости алгоритмов.
"""

from pathlib import Path
import csv
import platform
import sys

import matplotlib.pyplot as plt

from sorts_common import generate_data, measure
from algorithms import bubble_sort, insertion_sort
from m7_records import demo_stability, generate_records, bubble_sort_records, insertion_sort_records


SIZES = [1000, 2000, 3000, 4000, 5000]
REPEATS = 3
KIND = "duplicates"
LO, HI = 0, 10
SEED = 42


def run_experiment():
    results = {
        "bubble_sort": [],
        "insertion_sort": [],
    }

    for n in SIZES:
        data = generate_data(n, KIND, LO, HI, SEED)
        results["bubble_sort"].append(measure(bubble_sort, data, REPEATS))
        results["insertion_sort"].append(measure(insertion_sort, data, REPEATS))

    return results


def save_results(results):
    with open("results.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([
            "n", "bubble_sort_s", "insertion_sort_s",
            "bubble_T_n2", "insertion_T_n2",
            "bubble_over_insertion"
        ])
        for i, n in enumerate(SIZES):
            b = results["bubble_sort"][i]
            ins = results["insertion_sort"][i]
            writer.writerow([
                n, f"{b:.8f}", f"{ins:.8f}",
                f"{b / n**2:.12e}", f"{ins / n**2:.12e}",
                f"{b / ins:.4f}"
            ])


def save_plot(results):
    plt.figure(figsize=(9, 5.5))
    plt.plot(SIZES, results["bubble_sort"], marker="o", label="Пузырьком")
    plt.plot(SIZES, results["insertion_sort"], marker="o", label="Вставками")
    plt.xlabel("Размер массива n")
    plt.ylabel("Медианное время, с")
    plt.title("Вариант 17: время сортировки при большом числе повторов")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("lr2_plot.png", dpi=160)
    plt.close()


def save_system_info():
    with open("system_info.txt", "w", encoding="utf-8") as f:
        f.write(f"ОС: {platform.platform()}\n")
        f.write(f"Python: {sys.version.split()[0]}\n")
        f.write(f"Процессор: {platform.processor() or platform.machine()}\n")
        f.write("ОЗУ: определяется средствами ОС; для воспроизводимости важнее указать фактическое значение перед сдачей.\n")


def print_results(results):
    print("Вариант 17 — D [0; 10], k=3")
    print(f"{'n':>6} {'Пузырьком, с':>16} {'Вставками, с':>16} {'B/I':>10}")
    for i, n in enumerate(SIZES):
        b = results["bubble_sort"][i]
        ins = results["insertion_sort"][i]
        print(f"{n:>6} {b:>16.6f} {ins:>16.6f} {b/ins:>10.3f}")


if __name__ == "__main__":
    results = run_experiment()
    save_results(results)
    save_plot(results)
    save_system_info()
    demo_stability()
    print_results(results)
    print("\nРезультаты сохранены в results.csv, график — lr2_plot.png.")
