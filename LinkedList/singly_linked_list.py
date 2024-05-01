
class Node:
    def __init__(self,data):
        self.data = data;
        self.ref = None;

def traversal_linked_list(current):
    current = head
    while current is not None:
        print(current.data),
        current = current.ref;
    print()


head = Node(1);
second = Node(2);
third = Node(3);

head.ref= second
second.ref= third

traversal_linked_list(head);