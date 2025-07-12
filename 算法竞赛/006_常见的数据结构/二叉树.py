class TreeNode:
    """二叉树节点类"""

    def __init__(self, value):
        self.val = value
        self.left = None  # 左子节点
        self.right = None  # 右子节点


class BinaryTree:
    """二叉树实现"""

    def __init__(self):
        self.root = None  # 根节点

    def insert(self, value):
        """层序插入节点（保持完全二叉树结构）"""
        if not self.root:
            self.root = TreeNode(value)
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(value)
                return
            else:
                queue.append(node.left)

            if not node.right:
                node.right = TreeNode(value)
                return
            else:
                queue.append(node.right)


# 使用示例

tree = BinaryTree()
for val in [1, 2, 3, 4, 5, 6]:
    tree.insert(val)

