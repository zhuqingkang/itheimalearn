from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # 1. 从列表构建二叉树（层序遍历）
    # 层序遍历 表转树
    def list_to_tree(self, lst):
        if not lst:
            return None

        root = TreeNode(lst[0])
        queue = [root]
        i = 1

        while queue and i < len(lst):
            node = queue.pop(0)

            if i < len(lst) and lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1

            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1

        return root

    # 2. 二叉树转列表（层序遍历）
    def tree_to_list(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # 移除末尾多余的None
        while result and result[-1] is None:
            result.pop()

        return result


class TreeSolution:
    # 中序遍历二叉树
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res

    # 3. 前序遍历
    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    # 4. 中序遍历
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    # 5. 后序遍历
    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]

    # 6. 层序遍历
    def level_order(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result

