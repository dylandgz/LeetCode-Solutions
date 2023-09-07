
'''
Time Complexity: O(n) because we visit every node
Space Complexity: O(n) we use stack to store every node of the unsorted tree while it reaches the base case(leaf node)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # note that this is a depth first search tree
        # We will visit every node, and every time we will check their children and swap the position
        # do this recursively. Pre order or post order will work

        # create base case, if we reach a root that is None, then we just return None
        if not root:
            return None

        # swap the nodes with their subtrees
        temp = root.left
        root.left = root.right
        root.right = temp

        # recurse through the left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root