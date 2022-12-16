class MinHeap:
    def __init__(self):
        self.list = []

    def push(self, key):
        self.list.append(key)

        if (len(self.list) == 2):
            if self.list[0] > self.list[1]:
                self.list[0], self.list[1] = self.list[1], self.list[0]

        elif (len(self.list) > 2):
            self.minSort(self.list, len(self.list)-1)


    def minSort(self, list, index):
        
        child = index # last in the list
        parent = (child-1)//2
        if (list[child] < list[parent]):
            list[child], list[parent] = list[parent], list[child]
            if (parent >= 1):
                self.minSort(self.list, parent)
        

    def print(self):
        for i in range(0,len(self.list)):
            print(self.list[i], end = " ")
        print()

    def pop(self):
        length = len(self.list)
        if (length >= 3):
            self.list[0], self.list[length-1] = self.list[length-1], self.list[0]
            deleted = self.list[length-1]
            del self.list[length-1]
            self.pop_help(0)

        elif (length == 2):
            if (self.list[1] < self.list[0]):
                self.list[0], self.list[1] = self.list[1], self.list[0]
            deleted = self.list[1]
            del self.list[1]

        elif (length == 1):
            deleted = self.list[0]
            del self.list[0]

        else:
            return None

        return deleted

    def pop_help(self, index):
        currentVal = self.list[index]    

        if (len(self.list)-1 < 2*index+1):   # we dont have children :(
            return

        elif(len(self.list)-1 == 2*index+1):  # only left child
            rchild = None               
            lchild = self.list[2*index+1]
            lchildindex = 2*index+1
            if (lchild < currentVal):
                self.list[lchildindex], self.list[index] = self.list[index], self.list[lchildindex]
                self.pop_help(lchildindex)

        else:                               # both children
            lchild = self.list[2*index+1] 
            rchild = self.list[2*index+2]
            if (rchild <= lchild):
                min = rchild
                minindex = 2*index+2
            else:
                min = lchild
                minindex = 2*index+1

            if (min < currentVal):
                self.list[index], self.list[minindex] = self.list[minindex], self.list[index]
                self.pop_help(minindex)


                

if __name__ == "__main__":
    items = [9, 6, 4, 12, 7, 1, 3]
    heap = MinHeap()
    [heap.push(key) for key in items]
    heap.print()
    heap.pop()
    heap.print()
    heap.pop()
    heap.print()
   
    

    