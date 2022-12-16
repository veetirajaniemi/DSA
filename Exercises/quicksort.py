# Veeti Rajaniemi DSA W7 EX1


def qsort(A, i, j):
    pivotind = (i+j)//2 # finding a pivot
    A[pivotind], A[j] = A[j], A[pivotind] # pivot to the end
    left = partition(A, i, j-1, A[j]) # partitition for left subarray
    A[left], A[j] = A[j], A[left]

    if (left - i > 1):
        qsort(A, i, left -1)
    if (j - left > 1):
        qsort(A, left + 1, j)


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
    A = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]