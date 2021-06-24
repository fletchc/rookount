def getTetNum(n):
    return int((n*(n+1)*(n+2))/6)
# def getTriNum(n):

def isNotTetNum(n):
    k = 0
    while n >= getTetNum(k):
        if n == getTetNum(k):
            return 0
        k += 1
    return 1

def notTetNumConvolution(n):
    amount = 0
    for i in range(1, n + 1):
        amount += isNotTetNum(i) * (n - i + 1)
        print(isNotTetNum(i) * (n - i + 1), end=" ")
    print(amount)
    return amount

def wtfsequence(n):
    return int(((n+1)*(n**2 + 8*n + 18))/6)

def tritriangular(n):
    return int((n*(n+1)*(n-1)*(n-2))/8)

def triangular(n):
    return int((n*(n+1))/2)

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac

def nchoosek(n, k):
    return int(factorial(n)/(factorial(k) * factorial(n - k)))

def cattrap(n, k):
    m = 3
    if k < m and k >= 0:
        return nchoosek(n + k, k)
    elif m <= k and k <= n + m - 1:
        return nchoosek(n + k, k) - nchoosek(n + k, k - m)
    else:
        return 0


# for i in range(1, 10):
    # # print(notTetNumConvolution(getTetNum(i + 1) - 1))
    # notTetNumConvolution(getTetNum(i)-1)
# for i in range(10):
    # print(triangular(wtfsequence(i)) - nchoosek(nchoosek(i+3,2), 2)) 

for i in range(1, 10):
    print(nchoosek(nchoosek(6, 3), i))
print()

for i in range(1, 10):
    print(nchoosek(i + 1, 3))
    # print(getTetNum(i - 1))

# prints the values for the number of ways to place two nonattacking rooks
for i in range(1, 10):
    # print(triangular(cattrap(i, 3)) - nchoosek(nchoosek(i+2,2), 2)) 
    print(nchoosek(nchoosek(i + 1, 3), 2) - nchoosek(nchoosek(i, 2), 2))


for i in range(1, 10):
    # print(triangular(cattrap(i - 2, 3)) - triangular(triangular(i - 1) - 1))
    print(triangular(cattrap(i - 2, 3)) - triangular(triangular(i - 1) - 1))
