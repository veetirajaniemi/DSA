# Veeti Rajaniemi 6.9.2022 DSA W1 T1


def isort(A):
    print(A)
    for i in range(1,len(A)): # i = index of list
        j = i-1 # previous
        while (j >=0 and A[j] > A[j+1]): # compares j and next one
            num1 = A[j] 
            num2 = A[j+1] 
            A[j+1] = num1
            A[j] = num2
            print(A)
            j = j-1 
        print()  
    return A
 


def main():
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)

# main()

if __name__ == "__main__":
    main()

