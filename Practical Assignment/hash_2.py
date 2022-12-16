class Node: # class for nodes in linked list
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
                    string = string + " -> " # forming the string to be printed
            current = current.next 
        print(string)


    def append(self, data): # add data to the end of the linked list
        newNode = Node(data,None)

        if (self.head.next == self.tail): # first value to the list
            self.head.next = newNode

        else:
            current = self.head
            while (current.getNext() != self.tail):
                if (current.getNext().data == data or str(current.getNext().data) == data):
                    return
                current = current.next
            current.next = newNode

        newNode.next = self.tail
        self.len = self.len + 1


    def search(self, data):  # checking if certain value is in the list
        current = self.head
        for i in range(0,self.len):
            current = current.next
            if (current.data == data):
                return True       
        return False

    def delete(self, val): # deleting value from linked list
        current = self.head
        while(current.next != self.tail):
            if (current.next.data == val): # value found
                current.next = current.next.next
                self.len = self.len - 1 
                break
            current = current.next


class HashTable:
    def __init__(self, size):
        self.size = size
        self.T = [None]*size
        for i in range(0, size):
            self.T[i] = LinkedList() # implementing the linked list to every slot
                

    # using string folding to form keys for input values
    def hashValue(self, input):
        sum = 0
        strinput = str(input) # input as a string to calculate hash value
        length = len(strinput)
        mul = 1
        for i in range(0,length):
            if (i % 4 == 0):
                mul = 1
            else:
                mul = mul * 256
            sum = sum + (ord(strinput[i])) * mul
        key = sum % self.size
            
        return key



    def insert(self, x): # adding value to the hash table
        key = self.hashValue(x) # searching the key to find correct list 
        self.T[key].append(x) # adding value to correct slot


    def delete(self, x): # deleting value from the hash table
        key = self.hashValue(x)
        if (self.T[key].search(x) == True): # checking that data is in the hash table
            self.T[key].delete(x) # deleting the value
    

    def search(self, x): # checking if x is in the hash table
        key = self.hashValue(x)
        return self.T[key].search(x)

    
    def print(self):
        for i in range(0,self.size):
            print(f"Slot number {i}:", end = " ")
            self.T[i].print()
        print()



if __name__ == "__main__":
    table = HashTable(3)
    table.insert(12)
    print("Added 12.") 
    table.print()
    table.insert("hashtable")
    print("Added 'hashtable'.")
    table.print()
    table.insert(1234)
    print("Added 1234.")
    table.print()
    table.insert(4328989)
    print("Added 4328989.")
    table.print()
    table.insert("BM40A1500")
    print("Added 'BM40A1500'.")
    table.print()
    table.insert(-12456)
    print("Added -12456.")
    table.print()
    table.insert("aaaabbbbcccc")
    print("Added 'aaaabbbbcccc'.")
    table.print()


    print("Searching for -12456: " + str(table.search(-12456)))
    print("Searching for 'hashtable': " + str(table.search("hashtable")))
    print("Searching for 1235: " + str(table.search(1235)))
    print()

    table.delete("BM40A1500")
    table.delete(1234)
    table.delete("aaaabbbbcccc")
    print("Deleted 'BM40A1500', 1234 and 'aaaabbbbcccc'.")
    table.print()
