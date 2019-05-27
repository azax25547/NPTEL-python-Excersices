import re
text = 'ha hahaha ha'


inp_str = input()
count_list = []
for char in inp_str:
    if not char.isalnum():
        pass
    else:
        if inp_str.count(char) > 1:
            count_list.append(char)
        else:
            pass
print(count_list)
