// Author: RT
// Date: 2022-07-17T11:41:11.631Z
// URL: https://leetcode.com/problems/longest-increasing-subsequence/

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut tails = vec![nums[0]];

        for i in 1..n {
            let curr = nums[i];
            if curr > tails[tails.len() - 1] {
                tails.push(curr);
            } else {
                // or use Vec.partition_point method
                let li = Self::bisect_left(&tails, curr);
                tails[li] = curr;
            }
        }

        tails.len() as i32
    }

    fn bisect_left(xs: &Vec<i32>, x: i32) -> usize {
        let (mut l, mut r) = (0 as usize, xs.len());
        while l < r {
            let mid = l + (r - l) / 2;
            if xs[mid] >= x {
                r -= 1;
            } else {
                l += 1;
            }
        }

        l
    }
}
