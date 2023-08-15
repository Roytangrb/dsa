// Author: RT
// Date: 2023-08-15T04:53:33.588Z
// URL: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

int quickselect(int *nums, int n, int k, int l, int r) {
  int ptr = l;
  for (int i = l; i < r; i++) {
    if (nums[i] <= nums[r]) {
      int temp = nums[ptr];
      nums[ptr] = nums[i];
      nums[i] = temp;
      ptr++;
    }
  }
  int temp = nums[ptr];
  nums[ptr] = nums[r];
  nums[r] = temp;

  if (ptr == n - k) {
    return nums[ptr];
  } else if (ptr < n - k) {
    return quickselect(nums, n, k, ptr + 1, r);
  } else {
    return quickselect(nums, n, k, l, ptr - 1);
  }
}

int findKthLargest(int* nums, int numsSize, int k) {
  return quickselect(nums, numsSize, k, 0, numsSize - 1);
}
