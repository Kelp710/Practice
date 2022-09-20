from math import nextafter
from operator import length_hint, ne
from tkinter import NW


class Node():
    def __init__(self, data): #When instantiating a Node, we will pass the data we want the node to hold
        self.data = data 
        self.next = None 
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()
    def __repr__(self):
        """
        Return a dtring representation of the list
        Tskes O(n)
        :return:
        """
        node = []
        current = self.head

        while current:
            if current == self.head:
                node.append(f"[Head: {current.data}]")
            elif current.next ==  None:
                node.append(f"[Tail: {current.data}]")
            else:
                node.append(f"[{current.data}]")
            current = current.next
        return "->".join(node)

    def append(self, data):
        new_data = Node(data)
        if self.head == None:
            self.head = new_data
            self.tail = new_data
            self.length = 1
        else:
            self.tail.next = new_data
            self.tail.prev = self.tail
            self.tail = new_data
            self.length += 1
    
    def prepend(self, data):
        new_data = Node(data)
        if self.head == None:
            self.head = new_data
            self.tail = new_data
            self.length = 1
        else:
            self.head.prev = new_data
            new_data.next = self.head

            self.head = new_data
            self.length += 1

    def insert(self, index, data):
        new_data = Node(data)
        current_data = self.head
        if index == 0:
            self.prepend(data)
            self.length += 1
        if self.length == 0 or index > self.length:
            self.append(data)
            self.length += 1
        else:
            for n in range(index-1):
                current_data = current_data.next
            new_data.prev = current_data
            new_data.next = current_data.next
            current_data.next = new_data
            new_data = current_data.next.prev

            self.length += 1

        return self    

    def delete(self, index):
        current_data = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for n in range(index-1):
                current_data = current_data.next
            current_data.next = current_data.next.next
            if  current_data.next != None:
                current_data = current_data.next.prev
        

        




        

nodes = LinkedList()
nodes.append(10)
nodes.append(20)
nodes.append(42)
nodes.prepend(1)
nodes.delete(2)
nodes.insert(3, 99)
print(nodes)

