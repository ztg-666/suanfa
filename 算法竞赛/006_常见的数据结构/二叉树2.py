# 创建节点：值、左子树、右子树
def tree_node(value, left=None, right=None):
    return [value, left, right]


# 插入节点（层序插入）
def insert_tree(root, value):
    if root is None:
        return tree_node(value)

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node[1] is None:  # 左子树为空
            node[1] = tree_node(value)
            return root
        elif node[2] is None:  # 右子树为空
            node[2] = tree_node(value)
            return root
        else:
            queue.append(node[1])
            queue.append(node[2])
    return root


# 使用示例
root = None
for val in [1, 2, 3, 4, 5]:
    root = insert_tree(root, val)

