dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

total = input()


time = 0

for i in dial:
    for j in i:
        for x in total:
            if j == x :
                time += dial.index(i)+3
print(time)