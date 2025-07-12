class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    """单向链表类"""

    def __init__(self):
        self.head = None  # 链表头节点
        self.tail = None

    def append(self, value):
        """在链表末尾添加节点"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, value):
        """在链表头部插入节点"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, value):
        """在指定节点后插入新节点"""
        if not prev_node:
            print("错误：前一个节点不存在")
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        """删除包含指定值的节点"""
        current = self.head

        # 如果删除的是头节点
        if current and current.value == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.value != key:
            prev = current
            current = current.next

        if not current:
            return  # 未找到节点

        prev.next = current.next
        current = None

    def search(self, key):
        """查找包含指定值的节点"""
        current = self.head
        while current:
            if current.value == key:
                return True
            current = current.next
        return False

    def display(self):
        """打印链表内容"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))


# 使用示例
if __name__ == "__main__":
    # 创建链表并添加元素
    llist = LinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.prepend(5)

    # 打印链表: 5 -> 10 -> 20 -> 30
    llist.display()

    # 在10后面插入15
    node_10 = llist.head.next
    llist.insert_after(node_10, 15)
    llist.display()  # 5 -> 10 -> 15 -> 20 -> 30

    # 删除节点20
    llist.delete(20)
    llist.display()  # 5 -> 10 -> 15 -> 30

    # 查找元素
    print("元素15存在:", llist.search(15))  # True
    print("元素25存在:", llist.search(25))  # False
