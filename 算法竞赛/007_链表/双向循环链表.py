class Node:
    """双向链表节点类"""

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyCircularLinkedList:
    """双向循环链表类"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """检查链表是否为空"""
        return self.head is None

    def insert_at_begin(self, value):
        """在链表头部插入节点"""
        new_node = Node(value)
        if self.is_empty():
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    def insert_at_end(self, value):
        """在链表尾部插入节点"""
        if self.is_empty():
            self.insert_at_begin(value)
            return

        new_node = Node(value)
        tail = self.head.prev
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node

    def delete_node(self, key):
        """删除指定数据的节点"""
        if self.is_empty():
            return False

        current = self.head
        # 遍历查找目标节点
        while True:
            if current.value == key:
                # 处理单节点情况
                if current.next == current:
                    self.head = None
                else:
                    prev_node = current.prev
                    next_node = current.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    # 如果删除的是头节点
                    if current == self.head:
                        self.head = next_node
                return True
            current = current.next
            if current == self.head:  # 遍历完成
                break
        return False

    def display_forward(self):
        """正向打印链表数据"""
        if self.is_empty():
            print("链表为空")
            return

        current = self.head
        print("正向遍历: ", end="")
        while True:
            print(f"{current.value} -> ", end="")
            current = current.next
            if current == self.head:
                break
        print("(头节点)")

    def display_backward(self):
        """反向打印链表数据"""
        if self.is_empty():
            print("链表为空")
            return

        tail = self.head.prev
        current = tail
        print("反向遍历: ", end="")
        while True:
            print(f"{current.value} -> ", end="")
            current = current.prev
            if current == tail:
                break
        print("(尾节点)")


# 测试双向循环链表
if __name__ == "__main__":
    dcll = DoublyCircularLinkedList()

    # 插入数据
    dcll.insert_at_end(10)
    dcll.insert_at_begin(5)
    dcll.insert_at_end(20)
    dcll.insert_at_begin(1)

    # 显示链表
    dcll.display_forward()  # 输出: 1 -> 5 -> 10 -> 20 -> (头节点)
    dcll.display_backward()  # 输出: 20 -> 10 -> 5 -> 1 -> (尾节点)

    # 删除节点
    dcll.delete_node(5)
    dcll.display_forward()  # 输出: 1 -> 10 -> 20 -> (头节点)
