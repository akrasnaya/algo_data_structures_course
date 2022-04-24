"""
Задание.
Пункты, помеченные * реализуйте отдельно.

1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
delete(val, all=False)
где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.

1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).

1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка) -- clean()

1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный
 питоновский список найденных узлов).
find_all(val)

1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()

1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
insert(afterNode, newNode)
Если afterNode = None, добавьте новый элемент первым в списке.

* 1.7. Напишите проверочные тесты для каждого из предыдущих заданий.

* 1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений,
и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.

Рекомендации по тестированию.
Проверяйте случаи, когда список пустой, содержит много элементов и один элемент:
как в таких ситуациях будет работать удаление одного и нескольких элементов, вставка, поиск.
Особое внимание уделите корректности полей head и tail после всех этих операций.
"""

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
        return finded_nodes

    def delete(self, val, all=False):

        if self.head is not None:
            node = self.head
            while node.next is not None:
                if node.next.value == val:
                    node.next = node.next.next
                else:
                    node = node.next
                if all is False:
                    break


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


n1 = Node(12)
n2 = Node(55)
n3, n4, n5, n6, n7, n8, n9, n10, n11 = Node(20), Node(-7), Node(76), Node(-4), Node(33), Node(100), Node(56), Node(100), Node(-17)

n1.next = n2 # 12 -> 55
n2.next, n3.next, n4.next, n5.next, n6.next, n7.next, n8.next, n9.next, n10.next, n11.next = n3, n4, n5, n6, n7, n8, n9, n10, n11, None

big_list = LinkedList()

big_list.add_in_tail(n1)
big_list.add_in_tail(n2)
big_list.add_in_tail(n3)
big_list.add_in_tail(n4)
big_list.add_in_tail(n5)
big_list.add_in_tail(n6)
big_list.add_in_tail(n7)
big_list.add_in_tail(n8)
big_list.add_in_tail(n9)
big_list.add_in_tail(n10)
big_list.add_in_tail(n11)

small_list = LinkedList()
small_list.add_in_tail(Node(101))

empty_list = LinkedList()


