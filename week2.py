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


print(sumprimes([-3, 1, 6]))
# print(isprime(5))
# print(intreverse(3))
