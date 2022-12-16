def permutations(k,n,numbers):
    if (k == n):
        print(numbers)
    else:
        for i in range(1,n+1):
            if(included[i] != True):
                included[i] = True
                numbers[k] = i
                permutations(k+1,n,numbers)
                included[i] = False


if __name__ == "__main__":
    included = [None]*10
    numbers = [None]*5
    permutations(0,5,numbers)