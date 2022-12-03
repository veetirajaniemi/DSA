# Veeti Rajaniemi DSA W1 EX 2 060922

def primes(N):
    primes = 0
    if (N==2):
        primes = 1
    elif (N<=1):
        primes = 0
    else:
        primes = 1
        for i in range(3,N): # i is the number being tested
            isPrime = True
            for j in range(2,i-1):
                if (i%j == 0):
                    isPrime = False #not a prime, move to the next one
                    break
            if (isPrime == True):
                primes = primes + 1            
    return primes

def main():
    N = 9
    print(primes(N))
    
main()
