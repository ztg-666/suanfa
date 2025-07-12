# 约定俗成
# 用数组表示二叉树，下标为 i 的节点的 左孩子为 i * 2 + 1 右孩子为 i * 2 + 2

double_tree = [11,123123,-1,123,3213,-1,-1,11,123,-1,-1]

for i in range(len(double_tree)):
    if double_tree[i] == -1:
        print(f" 节点{i}为空节点")
        continue
    print(f"节点 {i} 值为: {double_tree[i]} , 孩子: 为 {2 * i + 1 } 和 {2 * i + 2}")