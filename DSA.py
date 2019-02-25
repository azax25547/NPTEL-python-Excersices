# python Data Structes N Algorithms
# Binary Search


def binary_serach(l, n):
    # first lets brake the list and go to middle
    length = len(l)
    ll = None
    arr = []
    if length % 2 == 0:
        ll = (length // 2) - 1
    else:
        ll = length // 2
    # print(ll)
    if n > l[ll]:
        for i in range(ll+1, length):
            arr.append(l[i])
    (binary_serach(arr, n))


binary_serach([1, 2, 3, 4, 5], 5)
