import time

dataset = [38, 27, 43, 3, 9, 82, 10]

def bubble_sort(arr):
    arr = arr[:]
    comp = swap = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
    return comp, swap

def insertion_sort(arr):
    arr = arr[:]
    comp = swap = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comp += 1
            arr[j+1] = arr[j]
            swap += 1
            j -= 1
        arr[j+1] = key
    return comp, swap

def quick_sort(arr):
    comp = swap = 0
    def _sort(arr):
        nonlocal comp, swap
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left  = [x for x in arr[1:] if (comp := comp+1) and x <= pivot]
        right = [x for x in arr[1:] if (comp := comp+1) and x > pivot]
        swap += len(left)
        return _sort(left) + [pivot] + _sort(right)
    _sort(arr[:])
    return comp, swap

def merge_sort(arr):
    comp = 0
    def _sort(arr):
        nonlocal comp
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left, right = _sort(arr[:mid]), _sort(arr[mid:])
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            comp += 1
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        return result + left[i:] + right[j:]
    _sort(arr[:])
    return comp, 0

# Run each and measure time
algos = [
    ("Bubble Sort",    bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Quick Sort",     quick_sort),
    ("Merge Sort",     merge_sort),
]

memory = {
    "Bubble Sort":    "In-place (low)",
    "Insertion Sort": "In-place (low)",
    "Quick Sort":     "Extra (medium)",
    "Merge Sort":     "Extra (medium)",
}

print(f"\nDataset: {dataset}\n")
print(f"{'Algorithm':<18} {'Comparisons':>13} {'Swaps':>7} {'Time (sec)':>13} {'Memory':>16}")
print("-" * 72)

for name, fn in algos:
    start = time.perf_counter()
    for _ in range(10000):
        comp, swap = fn(dataset)
    elapsed = (time.perf_counter() - start) / 10000
    print(f"{name:<18} {comp:>13} {swap:>7} {elapsed:>13.6f} {memory[name]:>16}")

print("-" * 72)