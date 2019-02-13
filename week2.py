
def intreverse(num):
    rev = ''
    while(num != 0):
        rev += str(num % 10)
        num = num // 10
    return rev


def isprime(l):
    prime = []
    for i in range(1, l+1):
        if l % i == 0:
            prime.append(i)
    if len(prime) == 2:
        return True
    else:
        return 0


def break_nums(l):
    for i in range(0, len(l)):
        result = map(isprime, l[i])
        resultList = list(result)
        if resultList[0] == True and resultList[1] == True:
            print(True)
        else:
            print(False)


def sumprimes(n):
    arr = []
    for i in range(1, n):
        for j in range(i, n):
            if i + j == n:
                arr.append([i, j])
    break_nums(arr)


sumprimes(7)


def rotateList(l, k):
    while k > 0:
        copy = l[0:1]
        l.pop(0)
        l = l + copy
        k = k-1
    return l
    # for i in range(0,k):
    #     copy = l[0:1]
    #     l.pop(0)
    #     l = l + copy


# def is_prime(lst):
#     count = 0
#     for i in range(0, len(lst)):
#         for j in range(1, lst[i]+1):
#             if lst[i] % j == 0:
#                 count = count + 1
#         if count == 2:
#             print("yea")


# def primepartiton(l):
#     for i in range(0,len(l)):
