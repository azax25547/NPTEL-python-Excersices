
# def break_nums(n):
#     arr = []
#     for i in range(1, n):
#         for j in range(i, n):
#             if i + j == n:
#                 arr.append([i, j])
#     return arr


# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def is_arr_prime(ar):
#     std_list = []
#     for i in range(0, len(ar)):
#         for j in range(0, 2):
#             # print(ar[i][j])
#             std_list.append(isprime(ar[i][j]))
#         if not std_list == [True, True]:
#             std_list = []
#         else:
#             return True


# def primepartition(l):
#     res = is_arr_prime(break_nums(l))
#     if res == None:
#         return False
#     else:
#         return True


# txt = "((jkl)78(A)&l(8(dd(FJI:),):)?)?"


# def nestingdepth(s):
#     f_p_count = s.count("(")
#     b_p_count = s.count(")")
#     if (f_p_count == b_p_count):
#         # print("true")
#         if s.find("(") == s.find(")") == -1:
#             # print(f_p_count,b_p_count)
#             return(0)
#         elif s.find("(") < s.find(")"):
#             print(f_p_count,b_p_count,3)

#             return(4)
#         else:
#             # print(f_p_count,b_p_count,2)

#             return(-1)
#     else:
#         print(f_p_count,b_p_count,1)
#         return(-1)


# # lol = nestingdepth(txt)
# # print(lol)


# def intreverse(num):
#     rev = ''
#     while(num != 0):
#         rev += str(num % 10)
#         num = num // 10
#     return rev


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


# def sumprimes(n):
#     arr = []
#     for i in range(1, n):
#         for j in range(i, n):
#             if i + j == n:
#                 arr.append([i, j])
#     break_nums(arr)


# # sumprimes(7)


# def rotateList(l, k):
#     while k > 0:
#         copy = l[0:1]
#         l.pop(0)
#         l = l + copy
#         k = k-1
#     return l
#     # for i in range(0,k):
#     #     copy = l[0:1]
#     #     l.pop(0)
#     #     l = l + copy


# # def is_prime(lst):
# #     count = 0
# #     for i in range(0, len(lst)):
# #         for j in range(1, lst[i]+1):
# #             if lst[i] % j == 0:
# #                 count = count + 1
# #         if count == 2:
# #             print("yea")


# # def primepartiton(l):
# #     for i in range(0,len(l)):

# def find_val_in_list(l, v):
#     for i in range(0, len(l)):
#         if l[i] == v:
#             return(l.index(l[i]))
#     else:
#         return(-1)


# # print(find_val_in_list([5, 2, 3], 3))

# def descend(l):
#     last = len(l) - 1
#     procedd = False
#     if l == []:
#         return True
#     else:
#         for i in range(last, 0, -1):
#             # print(l[i])
#             if l[i] < l[i-1] or l[i] == l[i-1]:
#                 procedd = True
#             else:
#                 return(False)
#     if procedd:
#         return True


# # print(descend([5,5,4,4,3,2,1]))

# def valley(l):
#     length = len(l)
#     begin = 0
#     if length <= 4:
#         return False
#     first = l[0]
#     last = l[-1]
#     mid = begin + length // 2
#     # return l[mid]
#     if first == last and first - l[mid] == last - l[mid] >= 2:
#         return True
#     else:
#         return False

# # print(valley([3,3,2,1,2]))


# def transpose(l):
#     length = len(l)
#     arr = []
#     if length == 1:
#         for item in l:
#             for it in item:
#                 arr.append([it])
#         print(arr)
#     elif length == 2:
#         l[0][1], l[1][1] = l[1][1], l[0][1]
#         print(l)



# # transpose([[1,2,3],[3,4,5]])
# def progression(l):
#     if len(l) == 1:
#         return(True)
#     # arr = []
#     length = len(l)-1
#     for i in range(length,1,-1):
#         # diff = l[i] - l[i-1]
#         # arr.append(diff)
#         if l[i] - l[i-1] == l[i-1] - l[i-2]:
#             return(True)
#         else:
#             return(False)
    
#     # for i in range(0, len(arr)-1):
#     #     if arr[i] != arr[i+1]:
#     #         return(False)
#     #     else:
#     #         return(True)

# # print(progression([3,5,7,9,10]))

# # myl = [[1,2,3], [4,5,6], [7,8,9]]
# # for i in range(0,len(myl)):
# #     myl[i].reverse()
# # popped = myl.pop(-1)
# # myl.append(popped)
# # print(myl)

def matrixflip(l,d):
    for i in range(0,len(l)):
        l[i].reverse()      # variant example and i/o
    if d == "v":
        # l[i].reverse()
        return(l)
    elif d== "h":
        l.reverse()
        popped = l.pop(-1)
        l.append(popped)
        return(l)

# print(matrixflip([[1,2],[3,4]],'h'))

score = {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}
keys = list(score.values())
# for i in range(0,len(keys)):
# print(keys)
arr = []
for i in range(0,len(keys)):
    # print(list(keys[i].values()))
    l = max(sorted(list(keys[i].values())))
    arr.append(l)
print(arr)
    