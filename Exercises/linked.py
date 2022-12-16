# Veeti Rajaniemi DSA W3 EX1

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def getNext(self):
        return self.next


class LinkedList:

    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0

    # prints the linked list
    def print(self):
        current = self.head
        string = ""
        
        
        while (current.getNext() != None):
            if (current.data != None):
                string = string + str(current.data)
                if (current.next.data != None):
                    string = string + " -> "
            current = current.next
        
        print(string)

        

    # add data to the end of the linked list
    def append(self, data):
        newNode = Node(data,None)

        if (self.head.next == self.tail):
            self.head.next = newNode

        else:
            current = self.head
            while (current.getNext() != self.tail):
                current = current.next
            current.next = newNode



        newNode.next = self.tail
        self.len = self.len + 1
        
    def insert(self, data, index):

        newNode = Node(data, None)

        current = self.head

        for i in range(0,index):
            current = current.next # previous before new node

        newNext = current.next
        current.next = newNode
        newNode.next = newNext

        self.len = self.len + 1

    def index(self, data):

        current = self.head
        index = None

        for i in range(0,self.len):
            current = current.next
            if (current.data == data):
                index = i
                break

        if (index == None):
            index = -1

        return index

    def delete(self, index):

        current = self.head

    

        if (index == 0):
            current.next = current.next.next
            self.len = self.len - 1

        else:
            if (index < self.len): 
                for i in range(0,index):
                    current = current.next

                current.next = current.next.next
                self.len = self.len - 1
            


if __name__ == "__main__":
    L = LinkedList() # only head and tail matter for L
    L.append(1)
    L.append(3)
    L.print()
    L.insert(10,1)
    L.insert(15,0)
    L.print()
    print(L.index(1))
    L.delete(0)
    L.print()


    

