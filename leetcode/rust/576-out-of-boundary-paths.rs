// Author: RT
// Date: 2022-07-16T15:58:22.327Z
// URL: https://leetcode.com/problems/out-of-boundary-paths/

impl Solution {
    pub fn find_paths(m: i32, n: i32, max_move: i32, start_row: i32, start_column: i32) -> i32 {
        let (m, n) = (m as usize, n as usize);
        const M: i32 = 1_000_000_007;
        let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

        let mut ans: i32 = 0;
        let mut dp = vec![vec![0; n]; m];
        dp[start_row as usize][start_column as usize] = 1;

        for _ in 0..max_move {
            let mut temp = vec![vec![0; n]; m];
            for i in 0..m {
                for j in 0..n {
                    if dp[i][j] == 0 {
                        continue;
                    }
                    let outbounds = (i == 0) as i32
                        + (i == m - 1) as i32
                        + (j == 0) as i32
                        + (j == n - 1) as i32;
                    // use loop instead of multiply to prevent overflow
                    for _ in 0..outbounds {
                        ans = ans % M + dp[i][j] % M;
                    }
                    for dir in dirs {
                        let x = (i as i32 + dir.0) as usize;
                        let y = (j as i32 + dir.1) as usize;
                        if (0..m).contains(&x) && (0..n).contains(&y) {
                            // to prevent overflow
                            temp[x][y] = temp[x][y] % M + dp[i][j] % M;
                        }
                    }
                }
            }
            dp = temp;
        }

        ans % M
    }
}
