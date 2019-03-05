# python Data Structes N Algorithms
# Binary Search


# def binary_serach(l, n):
#     # first lets brake the list and go to middle
#     first = 0
#     last = len(l) - 1
#     while first <= last:
#         mp = (first + last) / 2
#         if (l[mp] == n):
#             return mp
#         elif (l[mp] < n):
#             first = mp + 1
#         else:
#             last = mp - 1
#     return -1


# binary_serach([1, 2, 3, 4, 5], 4)

def bubble_sort(l):
    n = len(l)
    while 1:
        swapped = False
        for i in range(1, n):
            if l[i-1] > l[i]:
                (l[i-1], l[i]) = (l[i], l[i-1])
                swapped = True
        n = n-1
        if not swapped:
            break
    return l


# print(bubble_sort([7,5,1,9,0]))

'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''
def is_sum(l, e):
    for i in range(0, len(l)):
        for j in range(i, len(l)):
            try:
                if (l[i] + l[j+1] == e):
                    return True
                else:
                    pass
            except IndexError:
                pass
    return False


print(is_sum([10, 15, 3, 7], 17))
