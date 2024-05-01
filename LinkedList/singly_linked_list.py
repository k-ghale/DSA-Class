class Node:
    def __init__(self,data):
        self.data = data;
        self.ref = None;

class traversal_linked_list:
    def __init__(self):
        self.head = None 
    def print_LL(self):
        if self.head is None:
            print("Empty Linked List .")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref;

# head = Node();
# second = Node();
# third = Node();

# head.ref= second
# second.ref= third

LL1 = traversal_linked_list();
LL1.print_LL();
