// Author: RT
// Date: 2023-08-05T04:24:30.477Z
// URL: https://leetcode.com/problems/unique-binary-search-trees-ii/description/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode TreeNode;

TreeNode* alloc_node(int val, TreeNode *left, TreeNode *right) {
  TreeNode *node = malloc(sizeof *node);
  node->val = val;
  node->left = left;
  node->right = right;
  return node;
}

TreeNode** generate(int l, int r, int *count) {
  TreeNode **ans = NULL;
  
  if (l > r) {
    *count = 1;
    ans = malloc(sizeof *ans);
    ans[0] = NULL;
    return ans;
  }
  
  if (l == r) {
    *count = 1;
    TreeNode *root = alloc_node(l, NULL, NULL);
    ans = malloc(sizeof *ans);
    ans[0] = root;
    return ans;
  }

  int total = 0;
  int root_count = r - l + 1;
  TreeNode ***lis = malloc(root_count * sizeof *lis);
  int *li_cnts = malloc(root_count * sizeof(int));
  TreeNode ***ris = malloc(root_count * sizeof *ris);
  int *ri_cnts = malloc(root_count * sizeof(int));
  for (int rv = l, i = 0; rv <= r; rv ++, i ++) {
    int left_count, right_count;
    lis[i] = generate(l, rv - 1, &left_count);
    ris[i] = generate(rv + 1, r, &right_count);
    li_cnts[i] = left_count;
    ri_cnts[i] = right_count;
    total += left_count * right_count;
  }

  *count = total;
  ans = malloc(total * sizeof *ans);
  int j = 0;
  for (int rv = l, i = 0; rv <= r; rv ++, i ++) {
    for (int left_i = 0; left_i < li_cnts[i]; left_i ++){
      for (int right_i = 0; right_i < ri_cnts[i]; right_i ++){
	ans[j++] = alloc_node(rv, lis[i][left_i], ris[i][right_i]);
      }
    }
  }
  free(lis);
  free(ris);
  free(li_cnts);
  free(ri_cnts);
  return ans;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
TreeNode** generateTrees(int n, int* returnSize){
  return generate(1, n, returnSize);
}

