# Eetu Knutars helped to get the algorithm work without needing
# to sort the sumlist.  

def sums(items):

    sumall = sum(items)
    count = [0]*(sumall+1)

    sums = []
    sums.append(items[0])
    count[items[0]] = 1
    
    for i in range (1,len(items)):
        for j in range(0,len(sums)):
            if (count[items[i]+sums[j]] == 0):
                sums.append(items[i]+sums[j])
                count[items[i]+sums[j]] = 1
        if (count[items[i]] == 0):
            sums.append(items[i])
            count[items[i]] = 1

    return sum(count)


if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121