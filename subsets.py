def subsets(n: int) -> list:

    choice = [None]*n
    numlist = []
    subsetlist = [] 
    search(0, n, choice, numlist)
    numlist.pop(0)

    for list in numlist:
        list.reverse()
        subset = []
        for i in range(0,n):
            if (list[i] == 1):
                subset.append(i+1)
        subsetlist.append(subset)

    return subsetlist

def search(k, n, choice, numlist):
    if (k == n):
        numlist.append(choice[:])
        
    else:
        for i in range(0,2):
            choice[k] = i
            search(k+1, n, choice, numlist)


if __name__ == "__main__":
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]

    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]