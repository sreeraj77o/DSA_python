class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

if __name__ == "__main__":
    my_list = Linkedlist()

    print("Appending items: A, B, C")
    my_list.append("A")
    my_list.append("B")
    my_list.append("C")
    my_list.print_list()