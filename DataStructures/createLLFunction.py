class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        


def create_linked_list(input_list): # Complexity is O(n^2)
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

 
def create_linked_list_better(input_list): # Complexity is O(n) as it constantly refers to the tail which saves time in travering the entire LL, every single time
    
    head = None
    tail = None
    
    for value in input_list:
        
        if head is None:
            head = Node(value)
            tail = head            
        else:
            tail.next = Node(value)
            tail = tail.next        # update the tail
            
    return head


def print_linked_list(head_node):
    current_node = head_node

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next



        

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
print_linked_list(head)

print("Now the better version!!!")

input_list_2 = [4,76,4,54,543,76543,6,43,45]
head1 = create_linked_list_better(input_list_2)
print_linked_list(head1)
