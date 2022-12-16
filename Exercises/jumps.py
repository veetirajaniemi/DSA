# Eetu Knutars noticed that the case can be completed
# with only one for loop. 


def jumps(n,a,b):
    list = [0]*(n+1)
    list[0] = 1
    list[a] = 1
    for i in range(a+1,len(list)):
        list[i] = list[i-a]+list[i-b]
    return(list[n])


if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937

# Just for fun the previous attempts...:


    # def jumps(n, a, b):
#     list = [-1]*(n+1)
#     x = 0
#     return countjumps(n,a,b,list)


# def countjumps(n, a, b, list):

#     if (list[n] != -1):
#         return list[n]

#     if (n == 0):
#         list[n] = 1
#         return 1

#     elif (n < 0):
#         return 0

#     else:
#         count = countjumps(n-a,a,b,list) + countjumps(n-b,a,b,list)
#         return count


     # for i in range(a, b):
    #     if (i % a == 0):
    #         list[i] = i/a

    # if (b != 2):
    #     for i in range(b+1,n):
    #         list[i] = list[i-a] + list[i-b]
    # else:
    #     list[b] = 1
    #     for i in range(b+2,n):
    #         list[i] = list[i-a] + list[i-b]
# def jumps(n,a,b):
#     list = [0]*(n)
#     list[a-1] = 1
#     list[b-1] = 1
#     #print(list)

#     for i in range(a, b):
#         if (i % a == 0):
#             list[i] = i/a
#     #print(list)
#     for i in range(b, n):
#         list[i] = list[i-b] + list[i-a]    

#     print(list)
#     return(list[n-1])