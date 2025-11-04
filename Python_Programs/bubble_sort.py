from typing import List

def bubble_sort(arr: List[int]) -> None:
    """Sort array in-place using bubble sort."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    # Example usage
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before sorting: {numbers}")
    bubble_sort(numbers)
    print(f"After sorting:  {numbers}")

if __name__ == "__main__":
    main()