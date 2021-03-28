class LinkedList:
    head = None
    length = 0

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self.length += 1
            return self.Node.element
        node = self.head

        while node.next_node:
            node = node.next_node
        node.next_node = self.Node(element)
        self.length += 1
        return node.element

    def out(self):
        node = self.head
        while node.next_node:
            print(node.element, end=' ')
            node = node.next_node
        print(node.element)

    def insert(self, element, index):
        i = 0
        node = self.head

        while i < index:
            previous_node = node
            node = node.next_node
            i += 1

        previous_node.next_node = self.Node(element, next_node=node)
        self.length += 1
        print(f'Элемент {element}, был вствлен на {index} место')
        return element

    def get(self, index):
        i = 0
        node = self.head

        while i < index:
            previous_node = node
            node = node.next_node
            i += 1

        if node == self.head:
            return f'Элемент {node.element} является головным, ссылка на элемент {node.next_node.element}'
        elif node.next_node:
            return f'элемент = {node.element}, ссылка на элемент {node.next_node.element}'
        else:
            return f'Элемент {node.element} является последним'

    def delete(self, index):
        i = 0
        node = self.head

        while i <= index:
            previous_node = node
            node = node.next_node
            i += 1
        remove_elem = previous_node.element
        previous_node.element = node.element
        previous_node.next_node = node.next_node
        self.length -= 1
        print(f'Элемент {remove_elem} был удален')

    def get_len(self):
        return f'Длина списка = {self.length}'