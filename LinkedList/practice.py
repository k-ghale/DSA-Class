

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Traversed_LL:
    def __init__(self):
        self.head = None 

    def print_LL():
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next
       
       

class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def print__LinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

node1 = Node2(10)
node2 = Node2(20)
node3 = Node2(30)

node1.next = node2
node2.next = node3

print__LinkedList(node1)