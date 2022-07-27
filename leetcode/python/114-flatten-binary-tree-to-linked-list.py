# Author: RT
# Date: 2022-07-27T15:44:33.047Z
# URL: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


from .types import TreeNode


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.naive(root)

    def naive(self, root: TreeNode | None) -> None:
        """Store preorder and build linked list"""
        stack = []
        curr = root
        nodes = []

        while curr or stack:
            if curr:
                nodes.append(curr)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        for i in range(1, len(nodes)):
            prev = nodes[i - 1]
            curr = nodes[i]
            prev.left = None
            prev.right = curr

    def recursive(self, root: TreeNode | None) -> None:
        #    A       A
        #   / \       \
        #  B   C  =>   B
        #               \
        #                C
        def postorder(node: TreeNode | None) -> TreeNode | None:
            """return tail of converted linked list"""
            if not node:
                return None

            left = node.left
            right = node.right
            left_tail = postorder(left)
            right_tail = postorder(right)

            node.left = None
            node.right = left or right
            if left_tail:
                left_tail.right = right

            return right_tail or left_tail or node

        postorder(root)

    def stack(self, root: TreeNode | None) -> None:
        """Skew left subtree, rewire left tail to curr right, process right subtree"""
        if not root:
            return

        # state whether left subtree is processed
        DONE = True
        stack: list[tuple[TreeNode, bool]] = [(root, not DONE)]
        curr_tail = None

        while stack:
            node, done = stack.pop()

            if not node.left and not node.right:
                curr_tail = node
                continue

            if not done:
                if node.left:
                    stack.append((node, DONE))
                    stack.append((node.left, not DONE))
                elif node.right:
                    stack.append((node.right, not DONE))
            else:
                right = node.right

                if curr_tail:
                    curr_tail.right = node.right
                    node.right = node.left
                    node.left = None

                # continue process the right subtree
                if right:
                    stack.append((right, not DONE))
