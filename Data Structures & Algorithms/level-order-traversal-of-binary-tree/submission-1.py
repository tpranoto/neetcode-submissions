# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []

        fringe = deque()
        fringe.append(root)

        while fringe:
            l = len(fringe)
            level = []

            for i in range(l):
                node = fringe.popleft()
                level.append(node.val)
                if node.left:
                    fringe.append(node.left)
                if node.right:
                    fringe.append(node.right)
            
            if level:
                ans.append(level)
        
        return ans
        
        # ans = []
    
        # def dfs  (node, level):
        #     if node == None:
        #         return
        #     if len(ans) == level:
        #         ans.append([])
            
        #     ans[level].append(node.val)
        #     dfs(node.left,level+1)
        #     dfs(node.right,level+1)

        # dfs(root,0)
        # return ans
        
            
        