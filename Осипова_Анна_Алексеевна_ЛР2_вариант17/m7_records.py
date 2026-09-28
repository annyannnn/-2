"""Дополнительное задание М7: устойчивость сортировки записей."""


def bubble_sort_records(records):
    """Устойчивая сортировка пузырьком по сумме заказа."""
    a = records.copy()
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j][1] > a[j + 1][1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def insertion_sort_records(records):
    """Устойчивая сортировка вставками по сумме заказа."""
    a = records.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][1] > key[1]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def generate_records():
    return [
        ("Иванов", 1200),
        ("Петров", 800),
        ("Сидоров", 1200),
        ("Кузнецов", 500),
        ("Смирнов", 800),
        ("Попова", 1200),
    ]


def demo_stability():
    records = generate_records()
    bubble_result = bubble_sort_records(records)
    insertion_result = insertion_sort_records(records)

    assert bubble_result == [
        ("Кузнецов", 500),
        ("Петров", 800),
        ("Смирнов", 800),
        ("Иванов", 1200),
        ("Сидоров", 1200),
        ("Попова", 1200),
    ]
    assert insertion_result == bubble_result

    print("\nМ7 — демонстрация устойчивости")
    print("Исходные записи:", records)
    print("Пузырьком:", bubble_result)
    print("Вставками:", insertion_result)
