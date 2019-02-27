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


print(bubble_sort([7,5,1,9,0]))
