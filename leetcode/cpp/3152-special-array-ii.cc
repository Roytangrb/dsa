// https://leetcode.com/problems/special-array-ii/

class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        size_t n = nums.size();
        // prefix[i] stores how many pairs have same parity with nums[k+1]
        // for num[k] with k in [0, i)
        vector<int> prefix(n, 0);
        for (size_t i = 1; i < n; ++i) {
            int prev = nums[i-1], cur = nums[i];
            prefix[i] = prefix[i-1] + ((cur & 1) == (prev & 1));
        }

        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& v: queries) {
            ans.push_back(prefix[v[1]] - prefix[v[0]] == 0);
        }
        return ans;
    }
};
