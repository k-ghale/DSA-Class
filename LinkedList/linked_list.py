

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traversed_linked_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
        
    print()
    

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

traversed_linked_list(head);