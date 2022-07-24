// Author: RT
// Date: 2022-07-24T10:46:34.846Z
// URL: https://leetcode.com/problems/search-a-2d-matrix-ii/

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (m, n) = (matrix.len(), matrix[0].len());
        let (mut i, mut j) = (0, n - 1);

        // while i < m && j >= 0 {
        // j is wrapped to usize largest
        // Use match guards:
        while i < m {
            match matrix[i][j].cmp(&target) {
                std::cmp::Ordering::Less => i += 1,
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Greater if j > 0 => j -= 1,
                std::cmp::Ordering::Greater => break,
            }
        }

        false
    }
}
