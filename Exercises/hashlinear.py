# Veeti Rajaniemi, DSA W4 EX1

class HashLinear:
    def __init__(self, M):
        self.M = M
        self.T = [None]*M

    def hashValue(self, x):
        sum = 0
        y = len(x)
        for i in range(0,y):
            sum = sum + ord(x[i])
        index = sum % self.M
        return index

    def insert(self, x):
        index = self.hashValue(x)

        if (self.T[index] == None or self.T[index] == x):
            self.T[index] = x
            
        else:
            xx = False
            for i in range(index,self.M):
                if (self.T[i] == None and xx == False):
                    self.T[i] = x
                    xx = True
                    
            if (xx == False):
                for i in range(0,index):
                    if (self.T[i] == None and xx == False):
                        self.T[i] = x
                        xx = True


    def delete(self, x):
        index = self.hashValue(x)

        if (self.T[index] == x):
            self.T[index] = None
        else:
            deleted = False
            for i in range(index + 1, self.M):
                if (self.T[i] == x and deleted == False):
                    self.T[i] = None
                    deleted = True
                elif(self.T[i] == None):
                    deleted = True

            if (deleted == False):
                for i in range(0,index):
                    if (self.T[i] == x and deleted == False):
                        self.T[i] = None
                        deleted = True
                    elif(self.T[i] == None):
                        deleted = True



    def print(self):
        for i in range(0,self.M):
            if (self.T[i] != None):
                print(self.T[i], end = " ")

        print()

    


if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("f0o")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()
    table.delete("f0o")
    table.delete("Some arbitary string which is not in the table")
    table.print()
    table.delete("123")
    table.print()
