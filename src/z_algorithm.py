"""Z Algorithm for string pattern matching"""


def compute_z(s: str) -> list[int]:
    n = len(s)
    z_values = [0] * n

    left = right = 0
    for i in range(1, n):
        if i > right:
            # start expanding the z-box
            left = right = i
            while right < n and s[right] == s[right - left]:
                right += 1
            right -= 1
            z_values[i] = right - left + 1
        else:
            # operating inside the z-box
            if z_values[i - left] < right - i + 1:
                # if the matched substring at index i does not
                # stretch till right bound of z-box, just copy
                z_values[i] = z_values[i - left]
            else:
                # else keep expanding the z-box
                left = i
                while right < n and s[right] == s[right - left]:
                    right += 1
                right -= 1
                z_values[i] = right - left + 1

    return z_values


def leetcode2223(s: str) -> int:
    """Leetcode 2223

    Find sum of substring lengths, where each substring is a prefix of the input.
    """
    # first value in z array is 0
    # the input string s is a prefix of itself, add score of len(s)
    return sum(compute_z(s)) + len(s)


if __name__ == "__main__":
    testcases = (
        ("babab", 9),
        ("azbazbzaz", 14),
        ("aabaaa", 12),
        ("hhzjhhzjsoiz", 18),
    )

    for s, expected in testcases:
        print(f"{s=}, z array={compute_z(s)}")
        assert leetcode2223(s) == expected, f"{expected=}"
