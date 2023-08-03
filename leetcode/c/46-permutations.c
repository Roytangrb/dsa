// Author: RT
// Date: 2023-08-02T05:02:47.691Z
// URL: https://leetcode.com/problems/permutations/description/


int backtrack(int* nums, int w, int** ans) {
  // fill table with permutations using first w elements in
  // and return the count of permutations
  if (w == 0) return 0;
  if (w == 1) {
    ans[0][0] = nums[0];
    return 1;
  }
  int count = backtrack(nums, w - 1, ans);
  int row = count;
  int i, j, temp;
  for (i = 0; i < count; i ++) {
    // ans[:count] are permutations of nums[:w-1]
    // extend all prefix permutations with nums[w-1] to form
    // permutations where the w-i th element is nums[w-1]
    ans[i][w-1] = nums[w-1];
    // create new permutation by conceptually insert nums[w-1]
    // to different position except the last position
    for (j = 0; j < w - 1; j ++) {
      memcpy(ans[row], ans[i], w * sizeof(int));
      temp = ans[row][j];
      ans[row][j] = ans[row][w-1];
      ans[row][w-1] = temp;
      row ++;
    }
  }
  return row;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
  int count = 1;
  int i;
  for (i = 1; i <= numsSize; i ++) {
    count *= i;
  }

  int **ans = (int**)malloc(sizeof(int*) * count);
  int *column_sizes = (int*)malloc(sizeof(int) * count);
  for (i = 0; i < count; i++) {
    column_sizes[i] = numsSize;
    ans[i] = (int*)malloc(sizeof(int) * numsSize);
  }

  backtrack(nums, numsSize, ans);

  *returnSize = count;
  *returnColumnSizes = column_sizes;

  return ans;
}
