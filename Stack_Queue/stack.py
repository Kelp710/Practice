

from tkinter.messagebox import NO


class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.length = 0

class Stack(Node):
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0
         
    def peek(self):
        return self.top

    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
            self.length += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    def pop(self):
        if self.top == None:
            print("It`s empty")
        else:
            self.top.next = self.top
            self.length -= 1
            if self.length==0:
                self.bottom=None
    
    def stack_print(self):
        current = self.top
        if self.length ==0:
            print("It`s empty")
        else:
            for n in range(self.length):
                print(current.data)
                current = current.next



            

             

    
# class Stack():
#     def __init__(self) -> None:
#         self.array = []
     
#     def peek(self):
#         return self.array[len(self.array)-1]

#     def push(self, data):
#         self.array.append(data)

#     def pop(self):
#         if len(self.array) == 0:
#             return "Empty"
#         pop = self.array.pop()
#         return pop
#     def stack_print(self):
#         if len(self.array) == 0:
#             print("It`s empty")
#         else:
#             for n in range(len(self.array)-1, -1, -1):
#                 if n == 0:
#                     print(self.array[n])
#                 elif n == len(self.array)-1:
#                     print(self.array[n])
#                 else:
#                     print(self.array[n])

stack = Stack()
stack.push(2)
stack.push(4)
stack.push(6)
stack.peek()
stack.stack_print()