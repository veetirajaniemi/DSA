# DSA W5 EX1 Veeti Rajaniemi


class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

        

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
        else:
            self.insertNode(self.root, key)

        return


    def insertNode(self, currentRoot, key):
        if (key < currentRoot.key):
            if (currentRoot.left == None):
                currentRoot.left = Node(key)
            else:
                self.insertNode(currentRoot.left, key)

        elif (key > currentRoot.key):
            if (currentRoot.right == None):
                currentRoot.right = Node(key)
            else:
                self.insertNode(currentRoot.right, key)
                
        return


    def search(self, key):
        if (self.root.key == key):
            return True
        else:
            return self.searchNode(self.root, key)

            
    def searchNode(self, currentRoot, key):
        if (currentRoot.key == key):
            return True

        elif (currentRoot.key > key):
            if (currentRoot.left != None):
                return self.searchNode(currentRoot.left, key)
            return False  
        else:
            if (currentRoot.right != None):
                return self.searchNode(currentRoot.right, key)
            return False


    def preorder(self):
        if (self.root == None):
            return
        else:
            self.preorderRec(self.root)
        print()
        return


    def preorderRec(self, currentRoot):
        if (currentRoot != None):
            print(currentRoot.key, end = " ")
            self.preorderRec(currentRoot.left)
            self.preorderRec(currentRoot.right)
        return  

    def breadthfirst(self):
        if (self.root == None):
            return
        else:
            queue = []
            queue.append(self.root)
            self.breadthfirstRec(self.root, queue)
        print()

        

    def breadthfirstRec(self, currentRoot, queue):
        
        if (currentRoot != None):
            print(currentRoot.key, end = " ")
            queue.remove(currentRoot)
            
            queue.append(currentRoot.left)
            queue.append(currentRoot.right)

            for q in queue:
                self.breadthfirstRec(q, queue)
            
        return






    def remove(self, key):
        self.root = self.removeHelp(self.root, key)


    def removeHelp(self, currentRoot, key):
        if (currentRoot == None):
            return currentRoot

        if(currentRoot.key > key):
            currentRoot.left = self.removeHelp(currentRoot.left, key)


        elif(currentRoot.key < key):
            currentRoot.right = self.removeHelp(currentRoot.right, key)

        else: # key found
            if (currentRoot.left == None):
                return currentRoot.right
            elif (currentRoot.right == None):
                return currentRoot.left
            else: # 2 children
                max = self.getMax(currentRoot.left)
                currentRoot.key = max.key
                currentRoot.left = self.removeHelp(currentRoot.left, max.key)
        
        return currentRoot




    def getMax(self, currentRoot):
        if (currentRoot.right == None):
            return currentRoot
        else:
            return self.getMax(currentRoot.right)



if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()
    Tree.breadthfirst()

   
    

