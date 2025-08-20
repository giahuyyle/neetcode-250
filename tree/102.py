# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # quick return case 1: empty
        if not root:
            return []
        
        # quick return case 2: only 1 node
        if not (root.left or root.right):
            return [[root.val]]

        res = []

        # initialize queue
        q = collections.deque()
        q.append(root)

        # loop until queue is empty
        while q:
            same_level = []

            for _ in range(len(q)):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(same_level)
        
        return res