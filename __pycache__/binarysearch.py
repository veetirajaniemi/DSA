# Veeti Rajaniemi W3 EX2
# Sources: A book Tietorakenteet ja algoritmit, Antti Laaksonen (p. 35, Binäärihaku)


def search(A: list, item: int):
    
    start = 0
    end = len(A)-1

    while (start<=end):
        index = (start+end)//2  # Eetu Knutars told me about this great "//" operator

        if (A[index] == item):
            break

        elif (A[index] < item):          
            start = start + 1

        elif (A[index] > item):
            end = end - 1

    if (A[index] != item): # item not found
        index = -1

    return index


if __name__ == "__main__":
    A = [1, 2, 3, 6, 10, 15, 22, 27, 30, 31]
    print(search(A, 6))     # 3
    print(search(A, 7))     # -1
    print(search(A, 30))    # 8