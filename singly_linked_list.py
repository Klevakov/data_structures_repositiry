class LinkedList:
    head = None
    length = 0

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None) -> None:
            self.element = element
            self.next_node = next_node

    def append(self, element):
        """Adding a node to the end of the list."""
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

    def out(self) -> None:
        """Print all values of the nodes of the list"""
        node = self.head
        while node.next_node:
            print(node.element, end=' / ')
            node = node.next_node
        print(node.element)

    def insert(self, element, index: int):
        """Adding a node to the list at a specific place in the list by index."""
        i = 0
        node = self.head
        while i < index:
            previous_node = node
            node = node.next_node
            i += 1
        previous_node.next_node = self.Node(element, next_node=node)
        self.length += 1
        print(f'The node with the value "{element}" is added to the list at position "{index}"')
        return element

    def get(self, index: int) -> str:
        """Get information about a node by its ordinal number in the list."""
        i = 0
        node = self.head
        while i < index:
            previous_node = node
            node = node.next_node
            i += 1
        if node == self.head:
            return f'The node with the value "{node.element}" is the head and has a link to the next node with the value "{node.next_node.element}"'
        elif node.next_node:
            return f'The node with the value "{node.element}" has a link to the next node with the value "{node.next_node.element}"'
        else:
            return f'The node with the value "{node.element}" is the last one'

    def delete(self, index: int):
        """Deleting a node by its ordinal number in the list."""
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
        print(f'The node with the value "{remove_elem}" was deleted')

    def get_len(self) -> None:
        print(f'List length = " {self.length}"')


