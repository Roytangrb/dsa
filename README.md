# dsa

Data Structure and Algorithm

[Development Guide](https://github.com/Roytangrb/dsa/blob/master/CONTRIBUTING.md)

<details>
<summary>Binary Search</summary>

- [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) ([code](leetcode/python/222-count-complete-tree-nodes.py))
- [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) ([code](leetcode/python/1011-capacity-to-ship-packages-within-d-days.py))

</details>

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
  - [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) ([code](leetcode/python/872-leaf-similar-trees.py))
  - [Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) ([code](leetcode/python/1339-maximum-product-of-splitted-binary-tree.py))
- BFS Traversal
  - [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
  - [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)
- Fenwick Tree/Segment Tree
  - [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) ([code](leetcode/python/307-range-sum-query-mutable.py))
  - [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) ([code](leetcode/python/315-count-of-smaller-numbers-after-self.py))
  - [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) ([code](leetcode/python/732-my-calendar-iii.py))
- Self-balancing Trees
  - [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) ([code](leetcode/python/981-time-based-key-value-store.py))
  - [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) ([code](leetcode/python/732-my-calendar-iii.py))
  - [Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set/) ([code](leetcode/python/2336-smallest-number-in-infinite-set.py))
- Lowest Common Ancestor (LCA)
  - [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) ([code](leetcode/python/236-lowest-common-ancestor-of-a-binary-tree.py))
  - [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) ([code](leetcode/python/235-lowest-common-ancestor-of-a-binary-search-tree.py))
- [Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/) ([code](leetcode/python/652-find-duplicate-subtrees.py))

</details>

<details>
<summary>Bit Manipulation</summary>

- Bitset
  - [Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/) ([code](leetcode/python/318-maximum-product-of-word-lengths.py))
  - [Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) ([code](leetcode/python/1239-maximum-length-of-a-concatenated-string-with-unique-characters.py))
  - [Image Overlap](https://leetcode.com/problems/image-overlap/) ([code](leetcode/python/835-image-overlap.py))
- Unset Rightmost Bit
  - [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) ([code](leetcode/python/191-number-of-1-bits.py))
- Unset Leftmost Bit
  - [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) ([code](leetcode/python/1461-check-if-a-string-contains-all-binary-codes-of-size-k.py))
- Get Leftmost Set Bit
  - [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) ([Base 2 Long Division](leetcode/python/29-divide-two-integers.py))
- Get Rightmost Set Bit
  - [Power of Four](https://leetcode.com/problems/power-of-four/) ([code](leetcode/python/342-power-of-four.py))
  - [Set Mismatch](https://leetcode.com/problems/set-mismatch/) ([code](leetcode/python/645-set-mismatch.py))
- Is Power of 2 (popcount = 1)
  - [Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/) ([code](leetcode/python/1680-concatenation-of-consecutive-binary-numbers.py))
- [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/) ([code](leetcode/python/540-single-element-in-a-sorted-array.py))
- [Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/) ([py](leetcode/python/1318-minimum-flips-to-make-a-or-b-equal-to-c.py)) ([c](leetcode/c/1318-minimum-flips-to-make-a-or-b-equal-to-c.c))

</details>

<details>
<summary>Graph</summary>

- [Bipartite Graph](https://en.wikipedia.org/wiki/Bipartite_graph)
  - [Is Graph Bipartite](https://leetcode.com/problems/is-graph-bipartite/) ([code](src/bipartiteness.py))
  - [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) ([code](leetcode/python/886-possible-bipartition.py))
- BFS Unweighted Shortest Path
  - [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
  - [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) ([code](leetcode/python/126-word-ladder-ii.py))
  - [Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) ([code](leetcode/python/1293-shortest-path-in-a-grid-with-obstacles-elimination.py))
  - [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) ([code](leetcode/python/433-minimum-genetic-mutation.py))
  - [Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) ([code](leetcode/python/1926-nearest-exit-from-entrance-in-maze.py))
  - [As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) ([code](leetcode/python/1162-as-far-from-land-as-possible.py))
  - [Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/) ([code](leetcode/python/1129-shortest-path-with-alternating-colors.py))
  - [Jump Game IV](https://leetcode.com/problems/jump-game-iv/) ([code](leetcode/python/1345-jump-game-iv.py))
  - [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/description/) ([code](leetcode/python/934-shortest-bridge.py))
- Bridge of Graph
  - [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) ([Tarjan's bridge finding](src/tarjan_bridge_finding.py))
- Convex Hull
  - [Erect the Fence](https://leetcode.com/problems/erect-the-fence/) ([code](leetcode/python/587-erect-the-fence.py))
- Dijkstra Shortest Path
  - [Minimum Weighted Subgraph With the Required Paths](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/) ([code](src/dijkstra.py))
  - [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
  - [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
  - [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) ([code](leetcode/python/787-cheapest-flights-within-k-stops.py))
- Disjoint Set Union Find
  - [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) ([union by size](src/union_by_size.py))
  - [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) ([union by rank](src/union_by_rank.py))
  - [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)
  - [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
  - [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) ([code](leetcode/python/990-satisfiability-of-equality-equations.py))
  - [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) ([code](leetcode/python/947-most-stones-removed-with-same-row-or-column.py))
  - [Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) ([code](leetcode/python/1061-lexicographically-smallest-equivalent-string.py))
  - [Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/) ([code](leetcode/python/2421-number-of-good-paths.py))
- [Hamiltonian Path](https://en.wikipedia.org/wiki/Hamiltonian_path)
  - [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) ([code](leetcode/python/980-unique-paths-iii.py))
- Minimum Spanning Tree
  - [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
    - [Kruskal's Algorithm](src/kruskal_mst.py) with union find
    - [Prim's Algorithm](src/prim_mst.py) with priority queue
- Topological Sort
  - [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) ([code](src/topological_sort.py))
  - [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) ([code](leetcode/python/329-longest-increasing-path-in-a-matrix.py))
  - [Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) ([code](leetcode/python/1557-minimum-number-of-vertices-to-reach-all-nodes.py))
- Modelling/Simulation
  - [Escape the Spreading Fire](https://leetcode.com/problems/escape-the-spreading-fire/)
  - [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) ([code](leetcode/python/576-out-of-boundary-paths.py))
- Traversal
  - [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) ([code](leetcode/python/417-pacific-atlantic-water-flow.py))
  - [Word Search](https://leetcode.com/problems/word-search/) ([code](leetcode/python/79-word-search.py))
- Tree
  - [Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) ([code](leetcode/python/834-sum-of-distances-in-tree.py))
  - [Number of Nodes in the Sub-Tree With the Same Label](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/) ([code](leetcode/python/1519-number-of-nodes-in-the-sub-tree-with-the-same-label.py))
  - [Minimum Fuel Cost to Report to the Capital](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/) ([code](leetcode/python/2477-minimum-fuel-cost-to-report-to-the-capital.py))

</details>

<details>
<summary>Hash Map</summary>

- [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) ([code](leetcode/python/219-contains-duplicate-ii.py))
- [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) ([code](leetcode/python/523-continuous-subarray-sum.py))
- [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) ([code](leetcode/python/380-insert-delete-getrandom-o1.py))
- [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/) ([code](leetcode/python/1657-determine-if-two-strings-are-close.py))

</details>

<details>
<summary>Heap/Priority Queue</summary>

- [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) ([code](leetcode/python/692-top-k-frequent-words.py))
- [Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) ([code](leetcode/python/1354-construct-target-array-with-multiple-sums.py))
- [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) ([code](leetcode/python/630-course-schedule-iii.py))
- [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) ([code](leetcode/python/1338-reduce-array-size-to-the-half.py))
- [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) ([code](leetcode/python/659-split-array-into-consecutive-subsequences.py))
- [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) ([code](leetcode/python/871-minimum-number-of-refueling-stops.py))
- [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) ([code](leetcode/python/1383-maximum-performance-of-a-team.py))
- [Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/) ([code](leetcode/python/2136-earliest-possible-day-of-full-bloom.py))
- [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) ([code](leetcode/python/295-find-median-from-data-stream.py))
- [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) ([code](leetcode/python/1834-single-threaded-cpu.py))
- [IPO](https://leetcode.com/problems/ipo/) ([code](leetcode/python/502-ipo.py))
- [Minimize Deviation in Array](https://leetcode.com/problems/minimize-deviation-in-array/) ([code](leetcode/python/1675-minimize-deviation-in-array.py))
- [Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/) ([code](leetcode/python/2542-maximum-subsequence-score.py))

</details>

<details>
<summary>Iterator</summary>

- Peeking Iterator
  - [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) ([code](src/iter_nested_list.py))
- [Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) ([code](leetcode/python/1662-check-if-two-string-arrays-are-equivalent.py))

</details>

<details>
<summary>Linked List</summary>

- Two Pointers
  - [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) ([code](leetcode/python/160-intersection-of-two-linked-lists.py))
  - [Partition List](https://leetcode.com/problems/partition-list/) ([code](leetcode/python/86-partition-list.py))
  - [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) ([code](leetcode/python/234-palindrome-linked-list.py))
  - [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) ([code](leetcode/python/19-remove-nth-node-from-end-of-list.py))
  - [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) ([code](leetcode/python/2095-delete-the-middle-node-of-a-linked-list.py))
  - [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) ([code](leetcode/python/328-odd-even-linked-list.py))
- Floyd’s Tortoise and Hare
  - [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) ([code](leetcode/python/141-linked-list-cycle.py))
  - [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
  - [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) ([code](leetcode/python/287-find-the-duplicate-number.py))
- [My Calendar I](https://leetcode.com/problems/my-calendar-i/) ([code](leetcode/python/729-my-calendar-i.py))
- [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) ([code](leetcode/python/237-delete-node-in-a-linked-list.py))
- [Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/) ([code](leetcode/python/2130))

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
  - [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/) ([code](leetcode/python/1351-count-negative-numbers-in-a-sorted-matrix.py))
  - [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) ([code](leetcode/python/240-search-a-2d-matrix-ii.py))
  - [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) ([code](leetcode/python/378-kth-smallest-element-in-a-sorted-matrix.py))
- Spiral Matrix
  - [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) ([code](leetcode/python/6-zigzag-conversion.py))
- Yale Format
  - [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) ([code](src/yale_format.py))
- [Rotate Image](https://leetcode.com/problems/rotate-image/) ([code](leetcode/python/48-rotate-image.py))
- [Image Overlap](https://leetcode.com/problems/image-overlap/) ([code](leetcode/python/835-image-overlap.py))
- [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) ([code](leetcode/python/766-toeplitz-matrix.py))
- [Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/) ([code](leetcode/python/427-construct-quad-tree.py))

</details>

<details>
<summary>Queue</summary>

- [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) ([code](leetcode/python/622-design-circular-queue.py))

</details>

<details>
<summary>Sorting</summary>

- Binary Search
  - [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) ([code](leetcode/python/34-find-first-and-last-position-of-element-in-sorted-array.py))
  - [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) ([code](leetcode/python/378-kth-smallest-element-in-a-sorted-matrix.py))
  - [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) ([code](leetcode/python/658-find-k-closest-elements.py))
  - [Insert Interval](https://leetcode.com/problems/insert-interval/) ([code](leetcode/python/57-insert-interval.py))
  - [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) ([code](leetcode/python/352-data-stream-as-disjoint-intervals.py))
  - [Minimum Time to Complete Trips](https://leetcode.com/problems/minimum-time-to-complete-trips/) ([code](leetcode/python/2187-minimum-time-to-complete-trips.py))
  - [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) ([code](leetcode/python/875-koko-eating-bananas.py))
- Longest Increasing Subsequence (LIS)
  - [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) ([code](leetcode/python/300-longest-increasing-subsequence.py))
  - [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) ([DP/ O(nlogn) with Patience Sort](leetcode/python/354-russian-doll-envelopes.py))
- Quickselect
  - [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) ([code](leetcode/python/215-kth-largest-element-in-an-array.py))
  - [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) ([code](src/quickselect.py))
  - [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) ([code](leetcode/python/462-minimum-moves-to-equal-array-elements-ii.py))
  - [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/) ([code](leetcode/python/1539-kth-missing-positive-number.py))
- Quicksort
  - [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) ([code](src/quicksort.py))
  - [Sort an Array](https://leetcode.com/problems/sort-an-array/) ([code](leetcode/python/912-sort-an-array.py))
- Two Pointers
  - [Find Two Swapped in Sorted Array](https://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/) ([code](src/find_swapped.py))
  - [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) ([code](leetcode/python/88-merge-sorted-array.py))
  - [3Sum Closest](https://leetcode.com/problems/3sum-closest/) ([code](leetcode/python/16-3sum-closest.py))
  - [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/) ([code](leetcode/python/26-remove-duplicates-from-sorted-array.py))
- Greedy Using Sort
  - [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/) ([code](leetcode/python/948-bag-of-tokens.py))
  - [Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/) ([code](leetcode/python/2007-find-original-array-from-doubled-array.py))
  - [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/) ([code](leetcode/python/976-largest-perimeter-triangle.py))
  - [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) ([code](leetcode/python/1046-last-stone-weight.py))

</details>

<details>
<summary>Stack</summary>

- Monotonic Stack
  - [132 Pattern](https://leetcode.com/problems/132-pattern/) ([code](src/find_132_pattern.py))
  - [Jump Game VI](https://leetcode.com/problems/jump-game-vi/) ([code](leetcode/python/1696-jump-game-vi.py))
  - [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) ([code](leetcode/python/42-trapping-rain-water.py))
  - [Online Stock Span](https://leetcode.com/problems/online-stock-span/) ([code](leetcode/python/901-online-stock-span.py))
  - [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) ([code](leetcode/python/84-largest-rectangle-in-histogram.py))
  - [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) ([code](leetcode/python/907-sum-of-subarray-minimums.py))
  - [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) ([code](leetcode/python/739-daily-temperatures.py))
- [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)
- [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) ([code](leetcode/python/32-longest-valid-parentheses.py))
- [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) ([code](leetcode/python/232-implement-queue-using-stacks.py))

</details>

<details>
<summary>String Search & Pattern Matching</summary>

- DP
  - [Word Break](https://leetcode.com/problems/word-break/) ([code](leetcode/python/139-word-break.py))
  - [Concatenated Words](https://leetcode.com/problems/concatenated-words/) ([code](leetcode/python/472-concatenated-words.py))
  - [Edit (Levenshtein) distance](https://leetcode.com/problems/edit-distance/) ([code](leetcode/python/72-edit-distance.py))
- Longest Common Subsequence (LCS)
  - [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) ([code](leetcode/python/583-delete-operation-for-two-strings.py))
  - [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) ([code](leetcode/python/1143-longest-common-subsequence.py))
- Hashmap
  - [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) ([code](leetcode/python/890-find-and-replace-pattern.py), same as [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/))
  - [Word Subsets](https://leetcode.com/problems/word-subsets/) ([code](leetcode/python/916-word-subsets.py))
  - [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/) ([code](leetcode/python/974-subarray-sums-divisible-by-k.py))
  - [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) ([code](leetcode/python/438-find-all-anagrams-in-a-string.py))
  - [Naming a Company](https://leetcode.com/problems/naming-a-company/) ([code](leetcode/python/2306-naming-a-company.py))
- Rolling Hash
  - [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) ([code](leetcode/python/1461-check-if-a-string-contains-all-binary-codes-of-size-k.py))
  - [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) ([code](leetcode/python/28-find-the-index-of-the-first-occurrence-in-a-string.py))
- Sliding Window
  - [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) ([code](leetcode/python/3-longest-substring-without-repeating-characters.py))
  - [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) ([code](leetcode/python/904-fruit-into-baskets.py))
  - [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) ([code](leetcode/python/30-substring-with-concatenation-of-all-words.py))
  - [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) ([code](leetcode/python/718-maximum-length-of-repeated-subarray.py))
  - [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) ([code](leetcode/python/76-minimum-window-substring.py))
  - [Permutation in String](https://leetcode.com/problems/permutation-in-string/) ([code](leetcode/python/567-permutation-in-string.py))
- Trie
  - [Design File System](https://leetcode.com/problems/design-file-system/) ([code](src/file_system.py))
  - [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) ([code](leetcode/python/745-prefix-and-suffix-search.py))
  - [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) ([code](leetcode/python/1268-search-suggestions-system.py))
  - [Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/) ([code](leetcode/python/820-short-encoding-of-words.py))
  - [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) ([code](leetcode/python/336-palindrome-pairs.py))
  - [Word Search II](https://leetcode.com/problems/word-search-ii/) ([code](leetcode/python/212-word-search-ii.py))
  - [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) ([code](leetcode/python/211-design-add-and-search-words-data-structure.py))
  - [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) ([code](leetcode/python/2352-equal-row-and-column-pairs.py))
- Two/K Pointers
  - [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/) ([code](leetcode/python/792-number-of-matching-subsequences.py))
- Z Algorithm
  - [Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/) ([code](src/z_algorithm.py))

</details>

<details>
<summary>Others</summary>

- [Bin Packing](https://en.wikipedia.org/wiki/Bin_packing_problem)
  - [0-1 Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem)
    - [Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) ([code](leetcode/python/1235-maximum-profit-in-job-scheduling.py))
  - [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) ([code](leetcode/python/473-matchsticks-to-square.py))
- Combinatorics
  - [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/) ([code](leetcode/python/2444-count-subarrays-with-fixed-bounds.py))
- Information Theory
  - [Poor Pigs](https://leetcode.com/problems/poor-pigs/) ([code](leetcode/python/458-poor-pigs.py))
- Math & Geometry
  - [Can Make Arithmetic Progression From Sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) ([code](leetcode/python/1502-can-make-arithmetic-progression-from-sequence.py))
  - [Ugly Number](https://leetcode.com/problems/ugly-number/) ([code](leetcode/python/263-ugly-number.py))
  - [Rectangle Area](https://leetcode.com/problems/rectangle-area/) ([code](leetcode/python/223-rectangle-area.py))
  - [Minimum Rounds to Complete All Tasks](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/) ([code](leetcode/python/2244-minimum-rounds-to-complete-all-tasks.py))
  - [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) ([code](leetcode/python//149-max-points-on-a-line.py))
  - [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) ([code](leetcode/python/1071-greatest-common-divisor-of-strings.py))
  - [Add Digits](https://leetcode.com/problems/add-digits/) ([code](leetcode/python/258-add-digits.py))
  - [Bulb Switcher](https://leetcode.com/problems/bulb-switcher/) ([code](leetcode/python/319-bulb-switcher.py))
- Permutation
  - [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) ([code](leetcode/python/377-combination-sum-iv.py))
  - [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/) ([code](leetcode/python/1220-count-vowels-permutation.py))
  - [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) ([code](leetcode/python/784-letter-case-permutation.py))
  - [Orderly Queue](https://leetcode.com/problems/orderly-queue/) ([code](leetcode/python/899-orderly-queue.py))
- Parsing
  - [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) ([code](leetcode/python/393-utf-8-validation.py))
  - [Basic Calculator](https://leetcode.com/problems/basic-calculator/) ([code](leetcode/python/224-basic-calculator.py))
  - [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) ([code](leetcode/python/150-evaluate-reverse-polish-notation.py))
- DP
  - [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) ([code](leetcode/python/188-best-time-to-buy-and-sell-stock-iv.py))
  - [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) ([code](leetcode/python/309-best-time-to-buy-and-sell-stock-with-cooldown.py))
  - [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) ([code](leetcode/python/1770-maximum-score-from-performing-multiplication-operations.py))
  - [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)
  - [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) ([code](leetcode/python/718-maximum-length-of-repeated-subarray.py))
  - [Push Dominoes](https://leetcode.com/problems/push-dominoes/) ([code](leetcode/python/838-push-dominoes.py))
  - [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/) ([code](leetcode/python/790-domino-and-tromino-tiling.py))
  - [Decode Ways](https://leetcode.com/problems/decode-ways/) ([code](leetcode/python/91-decode-ways.py))
  - [Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) ([code](leetcode/python/1155-number-of-dice-rolls-with-target-sum.py))
  - [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) ([code](leetcode/python/334-increasing-triplet-subsequence.py))
  - [String Compression II](https://leetcode.com/problems/string-compression-ii/) ([code](leetcode/python/1531-string-compression-ii.py))
  - [Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) ([code](leetcode/python/1335-minimum-difficulty-of-a-job-schedule.py))
  - [Perfect Squares](https://leetcode.com/problems/perfect-squares/)
  - [Arithmetic Slices II](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) ([code](leetcode))
  - [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) ([code](leetcode/python/931-minimum-falling-path-sum.py))
  - [Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/) ([code](leetcode/python/926-flip-string-to-monotone-increasing.py))
  - [New 21 Game](https://leetcode.com/problems/new-21-game/) ([code](leetcode/python/837-new-21-game.py))
  - [Stone Game II](https://leetcode.com/problems/stone-game-ii/) ([code](leetcode/python/1140-stone-game-ii.py))
  - [Stone Game III](https://leetcode.com/problems/stone-game-iii/) ([code](leetcode/python/1406-stone-game-iii.py))
  - Kadane's Algorithm
    - [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) ([code](leetcode/python/918-maximum-sum-circular-subarray.py))
- Greedy
  - [Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/) ([code](leetcode/python/1328-break-a-palindrome.py))
  - [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) ([code](leetcode/python/12-integer-to-roman.py))
  - [Jump Game II](https://leetcode.com/problems/jump-game-ii/) ([code](leetcode/python/45-jump-game-ii.py))
  - [Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/) ([code](leetcode/python/2131-longest-palindrome-by-concatenating-two-letter-words.py))
  - [Longest Subsequence With Limited Sum](https://leetcode.com/problems/longest-subsequence-with-limited-sum/) ([code](leetcode/python/2389-longest-subsequence-with-limited-sum.py))
  - [Maximum Value at a Given Index in a Bounded Array](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/) ([code](leetcode/python/1802-maximum-value-at-a-given-index-in-a-bounded-array.py))
  - [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) ([code](leetcode/python/452-minimum-number-of-arrows-to-burst-balloons.py))
  - [Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) ([code](leetcode/python/1578-minimum-time-to-make-rope-colorful.py))

</details>
