class Node():
    def __init__(self, data): #When instantiating a Node, we will pass the data we want the node to hold
        self.data = data #The data passed during instantiation will be stored in self.data
        self.next = None #This self.next will act as a pointer to the next node in the list. When creating a new node, it always points to null(or None).


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0


    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1


    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1



    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next==None:
                self.tail = self.head
            self.length -= 1
            return
        while current_node.next!= None and current_node.next.data != data:

            current_node = current_node.next
        if current_node.next!=None:
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")


    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if position>=self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return

    def reverse_link(self):
        first = self.head
        second = first.next
        self.tail = self.head
        while second:
            third = second.next
            second.next = first 
            first = second
            second = third
        self.head.next = None
        self.head = first
        return






if __name__ == '__main__':

    my_linked_list = LinkedList()
    
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(7)
    my_linked_list.append(9)
    my_linked_list.print_list()
    my_linked_list.reverse_link()
    my_linked_list.print_list()