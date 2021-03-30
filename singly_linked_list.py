class LinkedList:
    head = None
    tail = None
    length = 0

    class Node:

        def __init__(self, value, next_node=None) -> None:
            self.value = value
            self.next_node = next_node

    def append(self, value):
        """Adding a node to the end of the list."""
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def out(self) -> None:
        """Print all values of the nodes of the list"""
        if not self.head:
            return print('The list is empty')
        node = self.head
        while node.next_node:
            print(node.value, end=' / ')
            node = node.next_node
        print(node.value)

    def insert(self, value, index: int):
        """Adding a node to the list at a specific place in the list by index."""
        node = self.head

        if index == 0:
            new_node = self.Node(value, next_node=node)
            self.head = new_node
            self.length += 1
            if self.length == 1:
                self.tail == new_node
            print(f'The node with the value "{value}" is added to the list at position "{index}"')
        else:
            i = 0
            while i < index:
                previous_node = node
                if i == index - 1 and index == self.length:
                    node.next_node = self.Node(value)
                    self.length += 1
                    return print(f'The node with the value "{value}" is added to the list at position "{index}"')
                node = node.next_node
                i += 1
            previous_node.next_node = self.Node(value, next_node=node)
            self.length += 1
            print(f'The node with the value "{value}" is added to the list at position "{index}"')

    def get(self, index: int) -> str:
        """Get information about a node by its ordinal number in the list."""
        i = 0
        node = self.head
        while i < index:
            previous_node = node
            node = node.next_node
            i += 1
        if node == self.head:
            return f'The node with the value "{node.value}" is the head and has a link to the next node with the value "{node.next_node.value}"'
        elif node.next_node:
            return f'The node with the value "{node.value}" has a link to the next node with the value "{node.next_node.value}"'
        else:
            return f'The node with the value "{node.value}" is the last one'

    def delete(self, index: int):
        """Deleting a node by its ordinal number in the list."""
        if self.length == 0:
            return print('Deletion is not possible. List is empty.')
            # raise IndexError('Deletion is not possible. List is empty.')
        if index >= self.length:
            return print(f'Deletion is not possible. The list does not contain the {index} item')
            # raise IndexError(f'Deletion is not possible. The list does not contain the {index} item')
        if self.length == 1:
            remove_value = self.head.value
            self.tail = self.head = None
            self.length -= 1
            return print(f'The node with the value "{remove_value}" was deleted')
        if index == 0:
            self.head = self.head.next_node
            self.length -= 1
        else:
            i = 0
            node = self.head
            if index == self.length - 1:
                while i < index:
                    previous_node = node
                    node = node.next_node
                    i += 1
                remove_elem = node.value
                print(f'удаляем {remove_elem}')
                previous_node.next_node = None
                # НУжно ли тут прописать del node? для очистки памяти, ведь экземпляр класса создан, просто на него больше нет ссылок
                self.tail = previous_node
                self.length -= 1
                return print(f'The node with the value "{remove_elem}" was deleted')
            while i <= index:
                previous_node = node
                node = node.next_node
                i += 1
            remove_elem = previous_node.value

            previous_node.value = node.value
            previous_node.next_node = node.next_node
            self.length -= 1
            print(f'The node with the value "{remove_elem}" was deleted')

    def get_len(self) -> None:
        print(f'List length = " {self.length}"')


linked_list = LinkedList()

linked_list.out()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
linked_list.insert(100, 0)
linked_list.out()
linked_list.insert(100, 6)
linked_list.out()


# linked_list.get(2)
# linked_list.insert(80, 0)
# linked_list.out()
# linked_list.insert(800, 2)
# linked_list.out()
# linked_list.delete(0)
# linked_list.out()
# linked_list.delete(3)
# linked_list.out()
# print(linked_list.length)
# linked_list.delete(linked_list.length - 1)
# linked_list.out()