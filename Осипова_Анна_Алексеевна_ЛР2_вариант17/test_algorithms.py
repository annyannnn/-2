from algorithms import bubble_sort, insertion_sort
from m7_records import bubble_sort_records, insertion_sort_records

data = [3, 1, 2, 1, 0]
assert bubble_sort(data) == sorted(data)
assert insertion_sort(data) == sorted(data)
assert data == [3, 1, 2, 1, 0]

records = [("A", 2), ("B", 1), ("C", 2)]
expected = [("B", 1), ("A", 2), ("C", 2)]
assert bubble_sort_records(records) == expected
assert insertion_sort_records(records) == expected

print("All tests passed.")
