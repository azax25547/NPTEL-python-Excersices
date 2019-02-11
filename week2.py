
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
        return prime[1]
    else:
        return 0


def sumprimes(l):
    result = map(isprime, l)
    resultList = list(result)
    total_sum = sum(resultList)
    return total_sum

# arr = [1, 2, 3,4,5]
def rotateList(l,k):
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

print(rotateList([1,2,3,4,5],12))
# print(sumprimes([-3, 1, 6]))
# print(isprime(5))
# print(intreverse(3))
