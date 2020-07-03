class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    def to_list(self):
        
        sasank = list()
        head = self.head
        current = head
        while current is not None:
            sasank.append(current.value)
            current = current.next
        
        return sasank    
    
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next

print(linked_list.to_list())

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


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend