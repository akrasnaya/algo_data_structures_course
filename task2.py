class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        finded_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                finded_nodes.append(node)
            node = node.next
        return finded_nodes

    def delete(self, val, all=False):
        node = self.head
        if node is None:
            return
        elif node.value == val:
            self.head = node.next
            if node.next is None:
                self.tail = None
            else:
                self.head.prev = None
            if all is False:
                return
        else:
            while node is not None:
                if node.value == val and node.next is not None:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    if all is False:
                        break
                elif node.value == val and node.next is None:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return
                node = node.next


    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if self.head is None and afterNode is None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            if afterNode is None:
                self.add_in_tail(newNode)
            else:
                node = self.head
                while node is not None:
                    if node.value == afterNode.value:
                        if node.next is not None:
                            newNode.next = node.next
                            node.next.prev = newNode
                            node.next = newNode
                            newNode.prev = node
                        else:
                            node.next = newNode
                            newNode.prev = node
                            self.tail = newNode
                    node = node.next

    def add_in_head(self, newNode):
        newNode.next = self.head
        newNode.prev = None

        if self.head is not None:
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
