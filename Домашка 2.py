#Задание 1

class Node:
    def __init__(self, data):
        self.head = data
        self.next = None

class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.length = 0

    def add_forward(self, el):
        new_node = Node(el)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.length += 1

    def add_back(self, el):
        new_node = Node(el)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def pop(self, index=0):
        if index < 0 or index >= self.length:
            raise IndexError("pop index out of range")
        if index == 0:
            value = self.first.head
            self.first = self.first.next
            if self.first is None:
                self.last = None
        else:
            current = self.first
            for _ in range(index - 1):
                current = current.next
            value = current.next.head
            current.next = current.next.next
            if current.next is None:
                self.last = current
        self.length -= 1
        return value

    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError("can only concatenate LinkedList to LinkedList")
        result = LinkedList()
        current = self.first
        while current is not None:
            result.add_back(current.head)
            current = current.next
        current = other.first
        while current is not None:
            result.add_back(current.head)
            current = current.next
        return result

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("list index out of range")
        current = self.first
        for _ in range(index):
            current = current.next
        return current.head

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("list index out of range")
        current = self.first
        for _ in range(index):
            current = current.next
        current.head = value

    def __len__(self):
        return self.length

    def __str__(self):
        result = "("
        current = self.first
        while current is not None:
            result += str(current.head)
            if current.next is not None:
                result += " -> "
            current = current.next
        result += ")"
        return result

    def __repr__(self):
        return "LinkedList" + str(self)

#Задание 2


def swap_values(link_list, k):
    if k <= 0 or k > len(link_list):
        return
    left_node = link_list.first
    right_node = link_list.first
    for _ in range(k - 1):
        right_node = right_node.next
    for _ in range(len(link_list) - k):
        left_node = left_node.next
    left_node.head, right_node.head = right_node.head, left_node.head

#Задание 3

def alternating_split(link_list):
    '''
    Разбивает связанный список на два списка, содержащих чередующиеся элементы из исходного и возвращает эти списки
    '''
    list1 = LinkedList()  # Создаем первый список
    list2 = LinkedList()  # Создаем второй список
    current = link_list.first  # Устанавливаем текущий узел на первый узел исходного списка

    while current is not None:
        list1.append(current.head)  # Добавляем текущий узел в первый список
        current = current.next  # Переходим к следующему узлу
        if current is not None:
            list2.append(current.head)  # Добавляем следующий узел во второй список
            current = current.next  # Переходим к следующему узлу

    return list1, list2  # Возвращаем оба списка в виде кортежа