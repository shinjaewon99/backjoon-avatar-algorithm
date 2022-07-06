day = 0
arr = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

n , m = map(int,input().split())

for i in range(n-1):
    day = day +arr[i]
day = (day+m) %7

print(week[day])
