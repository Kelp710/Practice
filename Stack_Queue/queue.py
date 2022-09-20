class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.length = 0

class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        new_data = Node(data)
        if self.length == 0:
            self.first = self.last = new_data
            self.length += 1
            return
        else:
            self.last.next = new_data
            self.last = new_data
            self.length += 1
            return
    
    def dequeue(self):
        if self.length == 0:
            print("It`s empty")
            return
        else:
            if self.first == self.last:
                self.last = None
            self.first = self.first.next
            self.length -= 1
            return
    
    def queue_print(self):
        if self.length == 0:
            print("There is nothing")
            return
        else:
            current = self.first
            while current != None:
                print(current.data)
                current = current.next
            return
    
queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.queue_print()





    