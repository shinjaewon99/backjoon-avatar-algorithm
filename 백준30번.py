a= int(input())
arr= []

for i in range(a):
    num =(int(input()))
    if num == 0:
        arr.pop()
    else:
        arr.append(num)


print(sum(arr))