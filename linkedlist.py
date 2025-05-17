# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # store the data
        self.next = None  # pointer to the next node

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # start of the list

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:          # if list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:    # move to the end
                current = current.next
            current.next = new_node

    # Print all nodes
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Usage
my_list = LinkedList()
my_list.append("Ironman")
my_list.append("Thor")
my_list.append("Hulk")
my_list.print_list()


print('manually creating linked list ')
# Manually create and link nodes
n1 = Node("Ironman")
n2 = Node("Thor")
n3 = Node("Hulk")

n1.next = n2
n2.next = n3

# Traverse and print
current = n1
while current:
    print(current.data, end=' -> ')
    current = current.next
print("None")