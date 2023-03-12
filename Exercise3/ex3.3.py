import sys

lst = []
capacity = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)
    new_capacity = sys.getsizeof(lst)
    if new_capacity != capacity:
        print(
            f"Capacity changed from {capacity} bytes to {new_capacity} bytes at size {len(lst)}")
        capacity = new_capacity
