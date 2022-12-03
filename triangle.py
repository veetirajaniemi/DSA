#Veeti Rajaniemi DSA 080922 W1 EX3

def triangle(a,b,c):
    if (a <= 0 or b<=0 or c<=0):
        istriangle = False
    elif (a == b and b == c):
        istriangle = True
    else:
        if (a >= b and a >= c):
            biggest = a
            sm1 = b
            sm2 = c
        elif (b >=a and b >= c):
            biggest = b
            sm1 = a
            sm2 = c
        else:
            biggest = c
            sm1 = a
            sm2 = b
        
        if (sm1 + sm2 > biggest):
            istriangle = True
        else:
            istriangle = False

    return istriangle




def main():
    print(triangle(3, 5, 4))
    print(triangle(-1,2,3))
    print(triangle(5,9,14))
    print(triangle(30,12,29))

main()
