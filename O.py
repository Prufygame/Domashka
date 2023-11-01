# Задача 1 (Односвязный список)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, *args):
        '''
        У объекта класса есть три атрибута - первый узел, последний узел и длина списка. Данные атрибуты можно использовать только внутри класса
        '''
        self.head = None
        self.tail = None
        self.length = 0

        if len(args) > 0:
            for data in args:
                self.add_back(data)
        pass

    def add_forward(self, el):
        '''
        Добавляет элемент в начало списка со сложностью O(1)

        >>> l1 = LinkedList(1,2,3)
        >>> l1.add_forward(0)
        >>> print(l1)
        (0 -> 1 -> 2 -> 3)

        >>> l2 = LinkedList(l1, LinkedList(4,5, LinkedList(6,7)), 1)
        >>> print(l2)
        ((0 -> 1 -> 2 -> 3) -> (4 -> 5 -> (6 -> 7)) -> 1)
        >>> l2.add_forward(LinkedList(-2, -1))
        >>> print(l2)
        ((-2 -> -1) -> (0 -> 1 -> 2 -> 3) -> (4 -> 5 -> (6 -> 7)) -> 1)
        '''
        new_node = Node(el)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        pass

    def add_back(self, el):
        '''
        Добавляет элемент в конец списка со сложностью O(1)

        >>> l1 = LinkedList(1,2,3)
        >>> l1.add_back(4)
        >>> print(l1)
        (1 -> 2 -> 3 -> 4)

        >>> l2 = LinkedList(l1, LinkedList(5,6, LinkedList(7,8)), 9)
        >>> print(l2)
        ((1 -> 2 -> 3 -> 4) -> (5 -> 6 -> (7 -> 8)) -> 9)
        >>> l2.add_back(LinkedList(10, 11))
        >>> print(l2)
        ((1 -> 2 -> 3 -> 4) -> (5 -> 6 -> (7 -> 8)) -> 9 -> (10 -> 11))
        '''
        new_node = Node(el)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        pass

    def pop(self, index=0):
        '''
        Удаляет элемент списка на позиции index с конца и с начала cо сложностью O(1), а произвольный элемент списка за O(n),
        и возвращает значение удаленного элемента.

        >>> l1 = LinkedList(1, 2, 3, 4)
        >>> print(l1)
        (1 -> 2 -> 3 -> 4)
        >>> l1.pop()
        1
        >>> print(l1)
        (2 -> 3 -> 4)
        >>> l1.pop(1)
        3
        >>> print(l1)
        (2 -> 4)

        >>> l1.pop(10)
        Traceback (most recent call last):
            ...
        IndexError: pop index out of range
        '''
        if index >= self.length or index < -self.length:
            raise IndexError("pop index out of range")
        if index < 0:
            index = self.length + index
        if index == 0:
            value = self.head.data
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            value = prev_node.next.data
            prev_node.next = prev_node.next.next
            if index == self.length - 1:
                self.tail = prev_node
        self.length -= 1
        return value
        pass

    def __add__(self, other):
        '''
        other - только LinkedList обьект, в противном случае - ошибка

        >>> l1 = LinkedList(1, 2, 3)
        >>> l2 = LinkedList(4, 5)
        >>> l3 = l1 + l2
        >>> print(l3)
        (1 -> 2 -> 3 -> 4 -> 5)
        >>> print(l3 + [1, 2])
        Traceback (most recent call last):
            ...
        TypeError: can only concatenate LinkedList (not "list") to LinkedList
        >>> print(l3 + 1)
        Traceback (most recent call last):
            ...
        TypeError: can only concatenate LinkedList (not "int") to LinkedList
        '''
        if not isinstance(other, LinkedList):
            raise TypeError("can only concatenate LinkedList (not {}) to LinkedList".format(type(other).__name__))

        new_list = LinkedList()
        node = self.head
        while node:
            new_list.add_back(node.data)
            node = node.next

        other_node = other.head
        while other_node:
            new_list.add_back(other_node.data)
            other_node = other_node.next

        return new_list
        pass

    def __getitem__(self, index):
        '''
        Этот метод позволяет доступаться до элементов списка по индексу и возвращать значение элемента (сложность O(n)), например:

        >>> l1 = LinkedList(1,2,3)
        >>> l1[1]
        2
        >>> l1[0]
        1

        >>> l1[10]
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        '''
        if index >= self.length or index < -self.length:
            raise IndexError("list index out of range")
        if index < 0:
            index = self.length + index
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data
        pass

    def __setitem__(self, key, value):
        '''
        Этот метод позволяет присваивать значение элементу списка найденному по индексу (сложность O(n)), например:

        >>> l1 = LinkedList(1,2,3)
        >>> l1[1] = 5
        >>> l1
        LinkedList(1, 5, 3)
        >>> l1[10]
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        '''
        if key >= self.length or key < -self.length:
            raise IndexError("list index out of range")
        if key < 0:
            key = self.length + key
        node = self.head
        for _ in range(key):
            node = node.next
        node.data = value
        pass

    def __len__(self):
        '''
        Вызывается при передаче экземпляра класса LinkedList в встроенную функцию len() -> возвращается длина связанного списка

        >>> l1 = LinkedList(1,2,3)
        >>> len(l1)
        3
        '''
        return self.length
        pass

    def __str__(self):
        node = self.head
        values = []
        while node:
            values.append(str(node.data))
            node = node.next
        return "(" + " -> ".join(values) + ")"
        pass

    def __repr__(self):
        return str(self)
        pass


#Следующие две алгоритмические задачи требуется решать исключительно собственным созданным списком LinkedList
# без использования встроенных структур данных: list, tuple, set, dict, и т.д.

#Задача 2 (Подмена)

def swap_values(link_list, k):
    '''
    Учитывая связанный список, меняет местами k-ый элемент с самого начала с k-ым элементом с конца.  
    >>> l1 = LinkedList(1,2,3,4,5)
    >>> swap_values(l1, 2)
    >>> l1
    (1 -> 4 -> 3 -> 2 -> 5)
    '''
    if k >= len(link_list) or k < -len(link_list):
        raise IndexError("k index out of range")
    if k < 0:
        k = len(link_list) + k
    node1 = link_list.head
    for _ in range(k):
        node1 = node1.next
    node2 = link_list.head
    for _ in range(len(link_list) - k - 1):
        node2 = node2.next
    node1.data, node2.data = node2.data, node1.data
    pass


# Задача 3 (Передел)

def alternating_split(link_list):
    '''
    Разбивает связанный список на два списка, содержащих чередующиеся элементы из исходного и возвращает эти списки
    
    >>> alternating_split(LinkedList(1,2,3,4,5))
    (LinkedList(1, 3, 5), LinkedList(2, 4))

    '''
    list1 = LinkedList()
    list2 = LinkedList()
    node = link_list.head
    index = 0
    while node:
        if index % 2 == 0:
            list1.add_back(node.data)
        else:
            list2.add_back(node.data)
        node = node.next
        index += 1
    return list1, list2
    pass