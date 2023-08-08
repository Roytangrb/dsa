// Author: RT
// Date: 2023-08-08T04:59:29.738Z
// URL: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

int search(int* nums, int numsSize, int target){
  int l = 0, r = numsSize - 1;  // numsSize >= 1
  while (l < r) {
    int mid = l + (r - l) / 2;
    int curr = nums[mid];
    if (curr == target) {
      return mid;
    }
    if (curr >= nums[l]) {  // nums[l:mid+1] (the left half) is sorted
      if (nums[l] <= target && target < curr) {
	r = mid - 1;
      } else {
	l = mid + 1;
      }
    } else {  // nums[mid:] (the right half) is sorted
      if (curr < target && target <= nums[r]) {
	l = mid + 1;
      } else {
	r = mid - 1;
      }
    }
  }

  return nums[l] == target ? l : -1;
}
