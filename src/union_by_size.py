"""Union find algorithm, union by connected component size"""


def longest_consecutive_sequence(nums: list[int]) -> int:
    """Find length of longest consecutive seq in unsorted array, duplicates possible

    https://leetcode.com/problems/longest-consecutive-sequence/
    """
    n = len(nums)
    parent = [i for i in range(n)]
    size = [1] * n

    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            continue

        seen[num] = i
        if num - 1 in seen:
            union(i, seen[num - 1], parent, size)
        if num + 1 in seen:
            union(i, seen[num + 1], parent, size)

    return 0 if not size else max(size[i] for i in range(n) if find(i, parent) == i)


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, size):
    px = find(x, parent)
    py = find(y, parent)
    if px == py:
        return

    sx = size[px]
    sy = size[py]
    if sx >= sy:
        parent[py] = px
        size[px] += size[py]
    else:
        parent[px] = py
        size[py] += size[px]


if __name__ == "__main__":
    testcases = (
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 2, 0, 1], 3),
        ([], 0),
    )

    for nums, expected in testcases:
        assert longest_consecutive_sequence(nums) == expected
