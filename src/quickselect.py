"""Quickselect (Hoare Selection) algorithm to find top K/ Kth element(s)"""

import random
from collections import Counter


def partition(arr: list, left: int, right: int, pivot: int) -> int:
    """Lomuto's partition scheme, return pivot index of the partitioned list"""
    arr[pivot], arr[right] = arr[right], arr[pivot]

    for i in range(left, right):
        if arr[i] < arr[right]:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[left], arr[right] = arr[right], arr[left]

    return left


def quickselect(arr: list, left: int, right: int, k: int):
    if left >= right:
        return

    pivot = random.randint(left, right)
    pivot = partition(arr, left, right, pivot)

    if pivot == k:
        return
    elif pivot > k:
        quickselect(arr, left, pivot - 1, k)
    else:
        quickselect(arr, pivot + 1, right, k)


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return top K most frequent values in nums in any order"""
    # negative value to keep more frequent elements in the left partitions
    freqs = [(-freq, elm) for elm, freq in Counter(nums).items()]
    n = len(freqs)

    quickselect(freqs, 0, n - 1, k)

    return [elm for _, elm in freqs[:k]]


if __name__ == "__main__":
    testcases = (
        ([1], 1, [1]),
        ([1, 2], 2, [1, 2]),
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([5, 3, 1, 1, 1, 3, 5, 73, 1], 3, [1, 3, 5]),
    )

    for nums, k, expected in testcases:
        top_k = top_k_frequent(nums, k)
        print(f"{nums=}, {k=}, {top_k=}")
        assert list(sorted(top_k)) == expected, f"{expected=}"
