# 配列のインデックスiの親ノードや子ノードへのアクセスは次のように表現できます。

# 根ノード｜i = 1, 配列の先頭の要素
# 親ノード｜parent(i) = i / 2
# 左の子ノード｜left(i) = 2i
# 右の子ノード｜right(i)=2i+1
import sys 
class MaxHeap:

#The constructor initializes the heap with a maxsize entered by the user, size set to 0, all the elements of heap set to 0
#For the sake of easier calculation of parent and child nodes, we do the indexing from 1 instead of 0. So we fill the 0th index of heap with a garbage value
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

#Method to return the position of parent for the node currently at pos. Because of the 1-indexing the formula for the parents and children becomes simpler
    def parent(self, pos):
        return pos // 2

#Method to return the position of the left child for the node currently at pos
    def left_child(self, pos):
        return 2 * pos

#Method to return the position of the right child for the node currently at pos
    def right_child(self, pos):
        return (2 * pos) + 1

#Method that returns true if the passed node is a leaf node.
#All the nodes in the second half of the heap(when viewed as an array) are leaf nodes.
#So we just check if the position entered is >= half of the size of the heap and <= size of the heap
    def is_leaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

#Method to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

#Method to heapify the node at pos. This method will be called whenever the heap property is disturbed, to restore the heap property of the heap
#We will check if the concerned node is a leaf node or not first. If it is, then no need to do anything.
#If it is not and it is smaller than any of its children, then we will check which of its children is largest
#and swap the node with its largest child. After doing this, the heap property may be disturbed. So we will call max_heapify again.
    def max_heapify(self, pos):

        #If the node is a non-leaf node and smaller than any of its child
        if not self.is_leaf(pos):
            if (self.Heap[pos] < self.Heap[self.left_child(pos)] or
                    self.Heap[pos] < self.Heap[self.right_child(pos)]):

                #Swap with the left child and heapify the left child
                if self.Heap[self.left_child(pos)] > self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))

                #Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

#Method to insert a node into the heap . First we will increase the size of the heap by 1.
#Then we will insert the element to end of the heap. Now this new element may violate the heap property.
#So we will keep checking its value with its parent's value. And keep swapping it with its parent as long as the parent is smaller than the element.
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

#Method to print the contents of the heap in a detailed format
    def print_heap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

#Method to remove and return the maximum element from the heap . The maximum element will be at the root.
#So we will copy the element at the end of the heap into the root node and delete the last node, which will leave the heap property disturbed
#So we will finally call heapify on the root node to restore the heap property
    def extract_max(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.max_heapify(self.FRONT)
        return popped