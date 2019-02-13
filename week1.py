
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


txt = "((jkl)78(A)&l(8(dd(FJI:),):)?)?"


def nestingdepth(s):
    f_p_count = s.count("(")
    b_p_count = s.count(")")
    if (f_p_count == b_p_count):
        # print("true")
        if s.find("(") == s.find(")") == -1:
            # print(f_p_count,b_p_count)
            return(0)
        elif s.find("(") < s.find(")"):
            print(f_p_count,b_p_count,3)

            return(4)
        else:
            # print(f_p_count,b_p_count,2)

            return(-1)
    else:
        print(f_p_count,b_p_count,1)
        return(-1)


lol = nestingdepth(txt)
print(lol)

