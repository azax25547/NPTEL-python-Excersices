def find_val_in_list(l, v):
    for i in range(0, len(l)):
        if l[i] == v:
            return(l.index(l[i]))
    else:
        return(-1)


# print(find_val_in_list([5, 2, 3], 3))

def descend(l):
    last = len(l) - 1
    procedd = False
    if l == []:
        return True
    else:
        for i in range(last, 0, -1):
            # print(l[i])
            if l[i] < l[i-1] or l[i] == l[i-1]:
                procedd = True
            else:
                return(False)
    if procedd:
        return True


# print(descend([5,5,4,4,3,2,1]))

def valley(l):
    length = len(l)
    begin = 0
    if length <= 4:
        return False
    first = l[0]
    last = l[-1]
    mid = begin + length // 2
    # return l[mid]
    if first == last and first - l[mid] == last - l[mid] >= 2:
        return True
    else:
        return False

# print(valley([3,3,2,1,2]))


def transpose(l):
    length = len(l)
    arr = []
    if length == 1:
        for item in l:
            for it in item:
                arr.append([it])
        print(arr)                
    elif length == 2:
        l[0][1],l[1][1] = l[1][1],l[0][1]
        print(l)
    
        
transpose([[1,2,3],[3,4,5]])
