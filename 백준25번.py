arr = []


for i in range(9):
    k = int(input())
    arr.append(k)


print(max(arr))
print(arr.index(max(arr))+1)
