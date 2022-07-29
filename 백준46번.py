# 2750번

n = int(input())
arr= []


for i in range(n):
    arr.append(int(input()))


m = sorted(arr)


for i in range(len(m)):
    print(m[i])
