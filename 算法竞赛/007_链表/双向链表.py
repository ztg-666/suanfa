class Node:
    """双向链表节点类"""

    def __init__(self, value):
        self.value = value  # 节点数据
        self.prev = None  # 前驱节点指针
        self.next = None  # 后继节点指针


class DoublyLinkedList:
    """双向链表类"""

    def __init__(self):
        self.head = None  # 链表头节点
        self.tail = None  # 链表尾节点

    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None

    def insert_at_head(self, value):
        """在链表头部插入新节点"""
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, value):
        """在链表尾部插入新节点"""
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_head(self):
        """删除头部节点"""
        if self.is_empty():
            return None

        deleted_node = self.head
        if self.head == self.tail:  # 只有一个节点
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return deleted_node.value

    def delete_at_tail(self):
        """删除尾部节点"""
        if self.is_empty():
            return None

        deleted_node = self.tail
        if self.head == self.tail:  # 只有一个节点
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return deleted_node.value

    def forward_traversal(self):
        """正向遍历链表"""
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def backward_traversal(self):
        """反向遍历链表"""
        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")


# 使用示例
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # 插入操作
    dll.insert_at_head(10)
    dll.insert_at_head(20)
    dll.insert_at_tail(30)

    # 遍历测试
    print("正向遍历:")
    dll.forward_traversal()  # 输出: 20 <-> 10 <-> 30 <-> None

    print("反向遍历:")
    dll.backward_traversal()  # 输出: 30 <-> 10 <-> 20 <-> None

    # 删除操作
    print("删除头部:", dll.delete_at_head())  # 输出: 20
    print("删除尾部:", dll.delete_at_tail())  # 输出: 30

    # 最终链表
    print("剩余链表:")
    dll.forward_traversal()  # 输出: 10 <-> None
