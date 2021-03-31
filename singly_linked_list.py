from typing import Any, Union


class LinkedList:
    head = None
    tail = None
    length = 0

    class Node:

        def __init__(self, value: Any, next_node=None) -> None:
            self.value = value
            self.next_node = next_node

        def __str__(self):
            return f'The Node with value {self.value}'

    def append(self, value: Any) -> None:
        """Adding a node to the end of the list."""
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1
        print(f'{new_node} was added')

    def out(self) -> None:
        """Print all values of the nodes of the list"""
        if not self.head:
            print('The list is empty')
        else:
            node = self.head
            while node.next_node:
                print(node.value, end=' / ')
                node = node.next_node
            print(node.value)

    def insert(self, value: Any, index: int) -> None:
        """Adding a node to the list at a specific place in the list by index."""
        node = self.head
        if index == 0:
            new_node = self.Node(value, next_node=node)
            self.head = new_node
            self.length += 1
            if self.length == 1:
                self.tail == new_node
            print(f'{new_node}" was inserted to the list at position "{index}"')
        else:
            previous_node = self.get(index - 1)
            new_node = self.Node(value, next_node=previous_node.next_node)
            previous_node.next_node = new_node
            if index == self.length:
                self.tail = new_node
            self.length += 1
            print(f'The node with the value "{value}" was inserted to the list at position "{index}"')

    def get(self, index: int) -> Node:
        """Get information about a node by its ordinal number in the list."""
        i = 0
        node = self.head
        while i < index:
            previous_node = node
            node = node.next_node
            i += 1
        if node == self.head:
            print(f'The node with the value "{node.value}" is the head and has a link to the next node with the value "{node.next_node.value}"')
        elif node.next_node:
            print(f'The node with the value "{node.value}" has a link to the next node with the value "{node.next_node.value}"')
        else:
            print(f'The node with the value "{node.value}" is the last one')
        return node

    def pop(self, index: int) -> Union[Node, None]:
        """Deleting a node by its ordinal number in the list."""
        if self.length == 0:
            print('Deletion is not possible. List is empty.')
            return None
        if index >= self.length:
            print(f'Deletion is not possible. The list does not contain the {index} item')
            return None
        if self.length == 1:
            remove_node = self.head
            self.tail = self.head = None
            self.length -= 1
            print(f'{remove_node} was deleted.Now the list is empty')
            return remove_node
        if index == 0:
            remove_node = self.head
            self.head = self.head.next_node
            self.length -= 1
            print(f'{remove_node} was deleted.')
            return remove_node
        else:
            previous_node = self.get(index - 1)
            remove_node = previous_node.next_node
            previous_node.next_node = remove_node.next_node
            if index == self.length - 1:
                self.tail = previous_node
            self.length -= 1
            print(f'{remove_node} was deleted')
            return remove_node

    def get_len(self) -> int:
        print(f'List length = " {self.length}"')
        return self.length





linked_list = LinkedList()

linked_list.out()
linked_list.append(10)
linked_list.insert(80, 0)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
linked_list.insert(100, 0)
linked_list.out()
linked_list.insert(100, 7)
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