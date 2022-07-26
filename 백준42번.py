# 1568번

n = int(input())

count = 0

sing = 1

while n > 0:
    if sing > n:

        sing =1

    n -=sing
    sing += 1

    count += 1


print(count)

