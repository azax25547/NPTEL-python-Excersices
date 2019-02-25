def find_val_in_list(l, v):
    for i in range(0, len(l)):
        if l[i] == v:
            return(l.index(l[i]))
    else:
        return(-1)


# print(find_val_in_list([5, 2, 3], 3))

def descend(l):
    last = len(l) - 1
    for i in range(last, -1, -1):
        # print(l[i])
        if l[i] < l[i-1] or l[i] == l[i-1]:
            return(True)
        else:
            return(False)


print(descend([19, 17, 18, 7]))
