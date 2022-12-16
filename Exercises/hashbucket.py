# Veeti Rajaniemi, DSA W4 EX2

from operator import truediv


class HashBucket:
    def __init__(self, M, B):
        self.M = M
        self.T = [None]*M
        self.B = B
        self.overflow = []

    
    def hashValue(self, x):
        sum = 0
        y = len(x)
        for i in range(0,y):
            sum = sum + ord(x[i])
        key = sum % self.B
        return key



    def insert(self, x):
        key = self.hashValue(x)
    
        y = self.M//self.B
        index = key*y # where to start

        xIn = False
        
        for i in range(index, index + y):
            if (xIn == True):
                break

            if (self.T[i] == None):
                self.T[i] = x
                xIn = True
            elif (self.T[i] == x):
                xIn = True

        if (xIn == False):
            self.overflow.append(x)



    def delete(self, x):
        key = self.hashValue(x)
        y = self.M//self.B
        index = key*y

        deleted = False

        for i in range(index, index + y):
            if (deleted == True):
                break
            
            elif (self.T[i] == x):
                self.T[i] = None
                deleted = True

        if (deleted == False):
            for i in range(0,len(self.overflow)):
                if (self.overflow[i] == x):
                    self.overflow.pop(i)
                    break



    def print(self):
        for i in range(0,self.M):
            if (self.T[i] != None):
                print(self.T[i], end = " ")

        for i in range(0, len(self.overflow)):
            print(self.overflow[i], end = " ")

        print()




if __name__ == "__main__":
    table = HashBucket(8,4)
    table.insert("BM40A1500")
    table.insert("f0o")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()
    table.delete("f0o")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()
   
