class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)

    else:
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    return


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


def append(self, value):
    """ Append a value to the end of the list. """
    # TODO: Write function to append here
    if self.head is None:
        self.head = Node(value)
    else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    return


LinkedList.append = append

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    if self.head is None:
        return None
    else:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            else:
                current = current.next


LinkedList.search = search

linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    if self.head is None:
        return None
    else:
        current = self.head
        while current:
            if current.value == value:
                return current
            else:
                current = current.next
            

LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"