a = int(input())
arr = []

for i in range(a):
    w , h = map(int, input().split())
    arr.append((w,h))


for j  in arr:
    rank =1

    for k in arr:
        if j[0]<k[0] and j[1]<k[1]:
            rank +=1

    print(rank, end = " ")