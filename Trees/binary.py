from calendar import c
from operator import ne


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, data):
        new_node = Node(data)
        current = self.root
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            while (current.left != new_node) and (current.right != new_node):
                if current.data < data:
                    if current.left == None:
                        current.left = new_node
                        self.number_of_nodes += 1
                    else:
                        current = current.left
                elif current.data > data:
                    if current.right == None:
                        current.right = new_node
                        self.number_of_nodes += 1
                    else:
                        current = current.right
            return      

    def search(self, data):
        if self.number_of_nodes == 0:
            print("It`s empty")
        else:
            current = self.root
            while current != None:
                if current.data == data:
                    print("Found")
                elif current.data < data:
                    current = current.left
                elif current.data > data:
                    current = current.right
            print("there is non")

    def remove(self, data):
        if self.root == None:
            return False
    
    
            


tree = BST()
tree.insert(9)
tree.insert(10)
tree.insert(2)
tree.insert(5)
tree.insert(28)
tree.insert(40)
tree.insert(400)
print(tree.root.data)