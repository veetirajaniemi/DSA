def binpack(items, S):

    items.sort(reverse=True)
    bin = [[]*len(items) for i in range(0,len(items))]
    binsums = [0]*len(items)

    for i in range(0,len(items)): # values
        for j in range(0,len(items)):
            if (binsums[j]+items[i] <= S):
                bin[j].append(items[i])
                binsums[j] += items[i]
                break

    bin = [x for x in bin if x != []]

    return bin
    
    
    
 
if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")