def cut_rod1(p, n):
    if (n == 0):
        return 0
    q = -10000000
    for i in range(1,n+1):
        q = max(q, p[i-1] + cut_rod1(p,n-i-1))
    return q


def cut_rod2(p, n):
    #let r be a new array of size n+1
    r = [None]*(n+1)
    r[0] = 0
    for j in range(1,n+1):
        q = -100000
        for i in range(1,j+1): 
           q = max(q, p[i-1] + r[j-i])
        r[j-1] = q
    return r[n-1]

###  1  2  3  4  5
p = [1, 5, 8, 9, 10]
#print(cut_rod1(p,6))
print(cut_rod2(p,6))

