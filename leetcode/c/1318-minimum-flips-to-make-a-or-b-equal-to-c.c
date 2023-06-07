// Author: RT
// Date: 2023-06-07T04:02:13.047Z
// URL: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

int minFlips(int a, int b, int c)
{
    // if bit at c is unset, both set bit(s) in a and b needs to be unset
    // i.e., if bit is set on (a & b) but not c, we need to double count.
    int diff_mask = (a | b) ^ c;
    return __builtin_popcount(diff_mask) + __builtin_popcount(a & b & diff_mask);
}