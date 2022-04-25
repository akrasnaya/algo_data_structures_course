class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

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
        
        while self.head is not None and self.head.value == val:
            self.head = self.head.next
            if all is False:
                return

        if self.head is not None:
            node = self.head
            while node.next is not None:
                if node.next.value == val and node.next.next is not None:
                    node.next = node.next.next
                    if all is False:
                        break
                elif node.next.value == val and node.next.next is None:
                    node.next = None
                    self.tail = node
                    break
                else:
                    node = node.next


    def clean(self):
        LinkedList.__init__()

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    newNode.next = node.next
                    node.next = newNode
                node = node.next
