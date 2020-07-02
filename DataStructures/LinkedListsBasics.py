class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_linked_list(head_node):
    current_node = head_node

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


head = Node(2)
new_node = Node(1)
head.next = new_node

# The top 2 lines or simply: head.next = Node(1)

head.next.next = Node(4)

head.next.next.next = Node(3)
head.next.next.next.next = Node(5)
# print(head.next.value)
print_linked_list(head)
