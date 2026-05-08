def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(greater)

numbers = [10, 7, 8, 9, 1, 5]
print("Original List:", numbers)
print("Sorted List:", quick_sort(numbers))