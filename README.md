# dsa

Data Structure and Algorithm

[Development Guide](https://github.com/Roytangrb/dsa/blob/master/CONTRIBUTING.md)

<details>
<summary>Binary Tree</summary>

- Traversal/Modification
  - [Relink BST to Sorted Linked List](https://leetcode.com/problems/increasing-order-search-tree/) ([code](src/bst_relink.py))
  - [Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/) (O(1) space with [Morris Traversal](src/morris_traversal.py))
  - [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
  - [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) ([code](src/find_swapped.py))
  - [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) ([code](leetcode/python/105-construct-binary-tree-from-preorder-and-inorder-traversal.py))
  - [Binary Search Tree Iterator II](https://leetcode.com/problems/binary-search-tree-iterator-ii/) ([code](src/bst_iterator.py))
  - [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) ([code](leetcode/python/114-flatten-binary-tree-to-linked-list.py))
  - [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) ([code](leetcode/python/108-convert-sorted-array-to-binary-search-tree.py))
  - [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) ([code](leetcode/python/98-validate-binary-search-tree.py))
- BFS Traversal
  - [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
  - [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)
- Fenwick Tree/Segment Tree
  - [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) ([code](leetcode/python/307-range-sum-query-mutable.py))
  - [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) ([code](leetcode/python/315-count-of-smaller-numbers-after-self.py))
- Lowest Common Ancestor (LCA)
  - [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) ([code](leetcode/python/236-lowest-common-ancestor-of-a-binary-tree.py))
  - [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) ([code](leetcode/python/235-lowest-common-ancestor-of-a-binary-search-tree.py))

</details>

<details>
<summary>Bit Manipulation</summary>

- Bitset
  - [Maximum Product of Word Lenghts](https://leetcode.com/problems/maximum-product-of-word-lengths/) ([code](leetcode/python/318-maximum-product-of-word-lengths.py))
- Unset Rightmost Bit
  - [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) ([code](leetcode/python/191-number-of-1-bits.py))
- Unset Leftmost Bit
  - [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) ([code](leetcode/python/1461-check-if-a-string-contains-all-binary-codes-of-size-k.py))
- Leftmost Bit Position
  - [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) ([Base 2 Long Division](leetcode/python/29-divide-two-integers.py))
  - [Power of Four](https://leetcode.com/problems/power-of-four/) ([code](leetcode/python/342-power-of-four.py))

</details>

<details>
<summary>Graph</summary>

- [Bipartite Graph](https://en.wikipedia.org/wiki/Bipartite_graph)
  - [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/) ([code](src/bipartiteness.py))
- BFS Unweighted Shortest Path
  - [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
  - [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) ([code](leetcode/python/126-word-ladder-ii.py))
- Dijkstra Shortest Path
  - [Minimum Weighted Subgraph With the Required Paths](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/) ([code](src/dijkstra.py))
  - [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
  - [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
- Disjoint Set Union Find
  - [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) ([union by size](src/union_by_size.py))
  - [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) ([union by rank](src/union_by_rank.py))
  - [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)
  - [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
- Bridge of Graph
  - [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) ([Tarjan's bridge finding](src/tarjan_bridge_finding.py))
- Minimum Spanning Tree
  - [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
    - [Kruskal's Algorithm](src/kruskal_mst.py) with union find
    - [Prim's Algorithm](src/prim_mst.py) with priority queue
- Topological Sort
  - [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) ([code](src/topological_sort.py))
  - [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) ([code](leetcode/python/329-longest-increasing-path-in-a-matrix.py))
- Modelling/Simulation
  - [Escape the Spreading Fire](https://leetcode.com/problems/escape-the-spreading-fire/)
  - [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) ([code](leetcode/python/576-out-of-boundary-paths.py))

</details>

<details>
<summary>Heap/Priority Queue</summary>

- [Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) ([code](leetcode/python/1354-construct-target-array-with-multiple-sums.py))
- [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) ([code](leetcode/python/630-course-schedule-iii.py))
- [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) ([code](leetcode/python/1338-reduce-array-size-to-the-half.py))
- [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) ([code](leetcode/python/659-split-array-into-consecutive-subsequences.py))
- [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) ([code](leetcode/python/871-minimum-number-of-refueling-stops.py))

</details>

<details>
<summary>Iterator</summary>

- Peeking Iterator
  - [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) ([code](src/iter_nested_list.py))

</details>

<details>
<summary>Linked List</summary>

- Two Pointers
  - [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) ([code](leetcode/python/160-intersection-of-two-linked-lists.py))
  - [Partition List](https://leetcode.com/problems/partition-list/) ([code](leetcode/python/86-partition-list.py))
  - [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) ([code](leetcode/python/234-palindrome-linked-list.py))
- Floyd’s Tortoise and Hare
  - [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) ([code](leetcode/python/141-linked-list-cycle.py))
  - [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
  - [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) ([code](leetcode/python/287-find-the-duplicate-number.py))
- [My Calendar I](https://leetcode.com/problems/my-calendar-i/) ([code](leetcode/python/729-my-calendar-i.py))

</details>

<details>
<summary>Matrix</summary>

- Backtracking
  - [N-Queens](https://leetcode.com/problems/n-queens/) ([code](leetcode/python/51-n-queens.py))
- Pre-computation
  - [Range Sum Query 2D](https://leetcode.com/problems/range-sum-query-2d-immutable/) ([code](leetcode/python/304-range-sum-query-2d-immutable.py))
  - [Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) ([code](leetcode/python/1074-number-of-submatrices-that-sum-to-target.py))
  - [Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/) ([code](leetcode/python/363-max-sum-of-rectangle-no-larger-than-k.py))
- Search Space Reduction
  - [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) ([code](leetcode/python/240-search-a-2d-matrix-ii.py))
  - [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) ([code](leetcode/python/378-kth-smallest-element-in-a-sorted-matrix.py))
- Yale Format
  - [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) ([code](src/yale_format.py))

</details>

<details>
<summary>Sorting</summary>

- Binary Search
  - [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) ([code](leetcode/python/34-find-first-and-last-position-of-element-in-sorted-array.py))
  - [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) ([code](leetcode/python/378-kth-smallest-element-in-a-sorted-matrix.py))
- Longest Increasing Subsequence (LIS)
  - [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) ([code](leetcode/python/300-longest-increasing-subsequence.py))
  - [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) ([DP/ O(nlogn) with Patience Sort](leetcode/python/354-russian-doll-envelopes.py))
- Quickselect
  - [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) ([code](leetcode/python/215-kth-largest-element-in-an-array.py))
  - [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) ([code](src/quickselect.py))
  - [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) ([code](leetcode/python/462-minimum-moves-to-equal-array-elements-ii.py))
- Quicksort
  - [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) ([code](src/quicksort.py))
- Two Pointers
  - [Find Two Swapped in Sorted Array](https://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/) ([code](src/find_swapped.py))
  - [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) ([code](leetcode/python/88-merge-sorted-array.py))

</details>

<details>
<summary>Stack</summary>

- Monotonic Stack
  - [132 Pattern](https://leetcode.com/problems/132-pattern/) ([code](src/find_132_pattern.py))
  - [Jump Game VI](https://leetcode.com/problems/jump-game-vi/) ([code](leetcode/python/1696-jump-game-vi.py))
- [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)
- [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) ([code](leetcode/python/32-longest-valid-parentheses.py))

</details>

<details>
<summary>String Search & Pattern Matching</summary>

- Longest Common Subsequence (LCS)
  - [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) ([code](leetcode/python/583-delete-operation-for-two-strings.py))
- Hashmap
  - [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) ([code](leetcode/python/890-find-and-replace-pattern.py), same as [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/))
  - [Word Subsets](https://leetcode.com/problems/word-subsets/) ([code](leetcode/python/916-word-subsets.py))
- Rolling Hash
  - [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) ([code](leetcode/python/1461-check-if-a-string-contains-all-binary-codes-of-size-k.py))
- Sliding Window
  - [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) ([code](leetcode/python/3-longest-substring-without-repeating-characters.py))
  - [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) ([code](leetcode/python/30-substring-with-concatenation-of-all-words.py))
- Trie
  - [Design File System](https://leetcode.com/problems/design-file-system/) ([code](src/file_system.py))
  - [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) ([code](leetcode/python/745-prefix-and-suffix-search.py))
  - [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) ([code](leetcode/python/1268-search-suggestions-system.py))
  - [Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/) ([code](leetcode/python/820-short-encoding-of-words.py))
- Two/K Pointers
  - [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) ([code](leetcode/python/792-number-of-matching-subsequences.py))
- Z Algorithm
  - [Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/) ([code](src/z_algorithm.py))

</details>

<details>
<summary>Others</summary>

- [Bin Packing](https://en.wikipedia.org/wiki/Bin_packing_problem)
  - [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) ([code](leetcode/python/473-matchsticks-to-square.py))
- Information Theory
  - [Poor Pigs](https://leetcode.com/problems/poor-pigs/) ([code](leetcode/python/458-poor-pigs.py))
- Permutation
  - [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) ([code](leetcode/python/377-combination-sum-iv.py))
  - [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/) ([code](leetcode/python/1220-count-vowels-permutation.py))

</details>
