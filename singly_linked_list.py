from typing import Any


class LinkedList:
    """
    A singly linked list is a data structure that is a sequence of elements,
    each containing a value and a pointer to the next element in the list.
    """

    head = None
    tail = None
    length = 0

    class Node:
        """A class is a description of an element of a singly linked list. """

        def __init__(self, value: Any, next_node=None) -> None:
            self.value = value
            self.next_node = next_node

        def __str__(self):
            return f'The Node with value {self.value}'

    def append(self, value: Any) -> None:
        """Adding a node to the end of the list. """

        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1
        print(f'{new_node} was added. ')

    def out(self) -> str:
        """Print all values of the nodes of the list. """

        if not self.head:
            return 'The list is empty. '
        else:
            node = self.head
            res_str = ''
            while node.next_node:
                res_str += f' {node.value} /'
                node = node.next_node
            return res_str + f' {node.value}'

    def insert(self, value: Any, index: int) -> None:
        """Adding a node to the list at a specific place in the list by index. """

        if index < 0 or index >= self.length and index != 0:
            raise IndexError
        node = self.head
        if index == 0:
            new_node = self.Node(value, next_node=node)
            self.head = new_node
            self.length += 1
            if self.length == 1:
                self.tail == new_node
            print(f'{new_node}" was inserted to the list at position "{index}".')
        else:
            previous_node = self.get(index - 1)
            new_node = self.Node(value, next_node=previous_node.next_node)
            previous_node.next_node = new_node
            if index == self.length:
                self.tail = new_node
            self.length += 1
            print(f'The node with the value "{value}" '
                  f'was inserted to the list at position "{index}".')

    def get(self, index: int) -> Node:
        """Get information about a node by its ordinal number in the list. """

        if self.length == 0 or 0 > index > self.length - 1:
            raise IndexError
        i = 0
        node = self.head
        while i < index:
            previous_node = node
            node = node.next_node
            i += 1
        if node == self.head:
            print(f'The node with the value "{node.value}" is the head and has a '
                  f'link to the next node with the value "{node.next_node.value}".')
        elif node.next_node:
            print(f'The node with the value "{node.value}" has a link to the next '
                  f'node with the value "{node.next_node.value}".')
        else:
            print(f'The node with the value "{node.value}" is the last one.')
        return node

    def pop(self, index: int) -> Any:
        """Deleting a node by its ordinal number in the list. """

        if self.length == 0:
            raise IndexError
            print('Deletion is not possible. List is empty.')
            return None
        if index >= self.length:
            raise IndexError
            print(f'Deletion is not possible. '
                  f'The list does not contain the {index} item.')
            return None
        if self.length == 1:
            remove_node = self.head
            self.tail = self.head = None
            self.length -= 1
            print(f'{remove_node} was deleted.Now the list is empty.')
            return remove_node.value
        if index == 0:
            remove_node = self.head
            self.head = self.head.next_node
            self.length -= 1
            print(f'{remove_node} was deleted.')
            return remove_node.value
        else:
            previous_node = self.get(index - 1)
            remove_node = previous_node.next_node
            remove_value = remove_node.value
            previous_node.next_node = remove_node.next_node
            if index == self.length - 1:
                self.tail = previous_node
            self.length -= 1
            print(f'{remove_node} was deleted.')
            return remove_value

    def get_len(self) -> int:
        """Returns the length of the list. """

        print(f'List length = " {self.length}"')
        return self.length

    def assign(self, value: Any, index: int) -> Any:
        """The method replaces the node's value and returns the old value. """

        if index < 0 or self.length == 0 or index > self.length - 1:
            raise IndexError
        node = self.get(index)
        remove_value = node.value
        node.value = value
        return remove_value
