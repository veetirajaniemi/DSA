# Veeti Rajaniemi DSA W7 EX2

def sales(cars, customers) -> int:
    cars = qsort(cars, 0, len(cars)-1) # sorting lists with quicksort
    customers = qsort(customers, 0, len(customers)-1)
    max = len(cars)-1 # max price of a car not bought yet
    bought = 0 
    cindex = len(customers)-1
    for i in range(0, len(cars)):
        if (cindex < 0): # no more customers
            break
        if (customers[cindex] >= cars[max]): #car bought:) 
            bought += 1
            cindex -= 1   
        max -= 1
    return bought


def qsort(A, i, j):
    pivotind = (i+j)//2 # finding a pivot
    A[pivotind], A[j] = A[j], A[pivotind] # pivot to the end
    left = partition(A, i, j-1, A[j]) # partitition for left subarray
    A[left], A[j] = A[j], A[left]

    if (left - i > 1):
        qsort(A, i, left -1)
    if (j - left > 1):
        qsort(A, left + 1, j)
    return A

def partition(list, left, right, pivot): # left and right indexes, pivot as a number
    while (left <= right): # not crossed
        while (list[left] < pivot):
            left += 1
        while (right >= left and list[right] >= pivot):
            right -= 1
        if (right > left):
            list[left], list[right] = list[right], list[left]
    return left 


if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5   