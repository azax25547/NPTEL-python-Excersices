# # def break_nums(n):
# #     arr = []
# #     for i in range(1, n):
# #         for j in range(i, n):
# #             if i + j == n:
# #                 arr.append([i, j])
# #     print(arr)

# def isprime(l):
#     prime = []
#     for i in range(1, l+1):
#         if l % i == 0:
#             prime.append(i)
#     if len(prime) == 2:
#         return True
#     else:
#         return 0
# def break_nums(l):
#     for i in range(0, len(l)):
#         result = map(isprime, l[i])
#         resultList = list(result)
#         if resultList[0] == True and resultList[1] == True:
#             print(True)
#         else:
#             print(False)


def break_nums(n):
    arr = []
    for i in range(1, n):
        for j in range(i, n):
            if i + j == n:
                arr.append([i, j])
    return arr


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


arr = [3, 4]


def is_arr_prime(ar):
    std_list = []
    for i in range(0, len(ar)):
        for j in range(0, 2):
            # print(ar[i][j])
            std_list.append(isprime(ar[i][j]))
        if not std_list == [True, True]:
            std_list = []
        else:
            return True


def primepartition(l):
    res = is_arr_prime(break_nums(l))
    if res == None:
        return False
    else:
        return True


lol = primepartition(185)
print(lol)
