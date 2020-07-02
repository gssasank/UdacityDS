class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    for i in input_list:
        if head is None:
            head = Node(i)
            
        else:
            current = head
            while current.next is not None :
                current = current.next
            current.next = Node(i)
            
    
    
    return head


def print_linked_list(head_node):
    current_node = head_node

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next



        

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
print_linked_list(head)


