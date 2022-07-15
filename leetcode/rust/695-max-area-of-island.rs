// Author: RT
// Date: 2022-07-15T15:22:09.130Z
// URL: https://leetcode.com/problems/max-area-of-island/

impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        let mut ans: i32 = 0;

        for i in 0..m {
            for j in 0..n {
                ans = std::cmp::max(ans, Self::dfs(&mut grid, i, j, m, n));
            }
        }

        ans
    }

    fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize, m: usize, n: usize) -> i32 {
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return 0;
        }
        if (grid[i][j] == 0) {
            return 0;
        }

        grid[i][j] = 0;
        let mut area = 1;
        for dir in [0, 1, 0, -1, 0].windows(2) {
            let dx = dir[0] as usize;
            let dy = dir[1] as usize;
            area += Self::dfs(grid, i + dx, j + dy, m, n);
        }

        area
    }
}
