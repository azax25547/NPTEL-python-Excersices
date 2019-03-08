from functools import reduce
test = int(input())
arr = []
for i in range(test):
    arr.append(int(input()))
# print(arr)
result = (reduce((lambda x, y: x*y), arr))
print(result)
