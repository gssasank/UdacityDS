class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
new_node = Node(1)
head.next = new_node

print(new_node.value)
print(head.next.value)
