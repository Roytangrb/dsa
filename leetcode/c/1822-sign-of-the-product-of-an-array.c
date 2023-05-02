// Author: RT
// Date: 2023-05-02T02:05:15.369Z
// URL: https://leetcode.com/problems/sign-of-the-product-of-an-array/

int arraySign(int *nums, int numsSize)
{
    int ret = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] == 0)
        {
            return 0;
        }
        ret ^= nums[i];
    }
    // if sign bit is on, there are odd number of negative numbers
    return ret < 0 ? -1 : 1;
}