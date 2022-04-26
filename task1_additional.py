def add_lists(llist1, llist2):
    fin_list = LinkedList()
    if llist1.len() == llist2.len():
        node1 = llist1.head
        node2 = llist2.head
        while node1 and node2:
            fin_list.add_in_tail(Node(node1.value + node2.value))
            node1 = node1.next
            node2 = node2.next
    return fin_list
