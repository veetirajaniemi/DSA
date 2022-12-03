# Veeti Rajaniemi DSA W2 EX3

def split(T):
    length = len(T)
    L = [0] * length
    R = [0] * length
    count = 0

    for i in range(0,length):
        L[i] = T[i]
        R[i] = T[i]

    lMax = T[0]
    rMin = T[-1]

    for i in range(0,length):
        j = length-1-i

        if (T[i] > lMax):
            lMax = T[i]

        if (T[j] < rMin):
            rMin = T[j]
        
        L[i] = lMax
        R[j] = rMin

    for i in range(0,length-1):
        if (L[i] < R[i+1]):
            count = count + 1
   
    return count


if __name__ == "__main__":
    print(split([1,2,3,4,5])) # 4
    print(split([5,4,3,2,1])) # 0
    print(split([2,1,2,5,7,6,9])) # 3
    print(split([1,2,3,1])) # 0
