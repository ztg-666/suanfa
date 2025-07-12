class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # 存储子节点列表

    def add_child(self, child_node):
        self.children.append(child_node)

# 创建树
root = TreeNode("A")
child_b = TreeNode("B")
child_c = TreeNode("C")
root.add_child(child_b)
root.add_child(child_c)
child_b.add_child(TreeNode("D"))
