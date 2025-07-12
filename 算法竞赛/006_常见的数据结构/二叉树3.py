# 创建节点
def create_node(value):
    return {'value': value, 'left': None, 'right': None}


# 插入节点（层序插入）
def insert_dict(root, value):
    if root is None:
        return create_node(value)

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node['left'] is None:
            node['left'] = create_node(value)
            return root
        elif node['right'] is None:
            node['right'] = create_node(value)
            return root
        else:
            queue.append(node['left'])
            queue.append(node['right'])
    return root

# 使用示例
root = None
for val in ['A', 'B', 'C', 'D']:
    root = insert_dict(root, val)

