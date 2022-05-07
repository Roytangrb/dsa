# dsa

Data Structure and Algorithm

[Development Guide](https://github.com/Roytangrb/dsa/blob/master/CONTRIBUTING.md)

## Algorithms

<details>
<summary>Binary Tree</summary>

- In-order Traversal
  - [Relink BST to Sorted Linked List](https://leetcode.com/problems/increasing-order-search-tree/) ([code](src/bst_relink.py))
  - [Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/) (O(1) space with [Morris Traversal](src/morris_traversal.py))
  - [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
  - [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) ([code](src/find_swapped.py))
- Iterative Binary Tree Traversal
  - [Binary Search Tree Iterator II](https://leetcode.com/problems/binary-search-tree-iterator-ii/) ([code](src/bst_iterator.py))

</details>

<details>
<summary>Graph</summary>

- [Bipartite Graph](https://en.wikipedia.org/wiki/Bipartite_graph)
  - [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/) ([code](src/bipartiteness.py))
- Dijkstra Shortest Path
  - [Minimum Weighted Subgraph With the Required Paths](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/) ([code](src/dijkstra.py))
  - [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
- Disjoint Set Union Find
  - [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) ([union by size](src/union_by_size.py))
  - [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) ([union by rank](src/union_by_rank.py))
  - [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)
  - [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
- Minimum Spanning Tree
  - [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
    - [Kruskal's Algorithm](src/kruskal_mst.py) with union find
    - [Prim's Algorithm](src/prim_mst.py) with priority queue
- Topological Sort
  - [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) ([code](src/topological_sort.py))

</details>

<details>
<summary>Matrix</summary>

- Yale Format
  - [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) ([code](src/yale_format.py))

</details>

<details>
<summary>Sorting</summary>

- Quickselect
  - [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) ([code](src/quickselect.py))
- Quicksort
  - [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) ([code](src/quicksort.py))
- [Find Two Swapped in Sorted Array](https://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/) ([code](src/find_swapped.py))

</details>

<details>
<summary>Stack</summary>

- Monotonic Stack
  - [132 Pattern](https://leetcode.com/problems/132-pattern/) ([code](src/find_132_pattern.py))
- [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

</details>

<details>
<summary>String Search & Pattern Matching</summary>

- Trie
  - [Design File System](https://leetcode.com/problems/design-file-system/) ([code](src/file_system.py))
- Z Algorithm
  - [Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/) ([code](src/z_algorithm.py))

</details>
