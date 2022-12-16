# Veeti Rajaniemi DSA W2 EX2

def pairs(s):

    dist = 0
    first = True
    x = 1
    oneindexsum = 0
    sum = 0
    
    for i in range(1,len(s)+1):
        j = len(s) - i # 5 4 3 2 1 0 --> index of list 

        if (s[j] == "1"):
            if (first == True):
                oneindexsum = oneindexsum + j
                
            if (first == False):
                sum = oneindexsum - x*j
                oneindexsum = oneindexsum + j
                x = x+1
                
            dist = dist + sum
            first = False 

               

    return dist
    

if __name__ == "__main__":
    
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71
