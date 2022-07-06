words = input().upper()
total = list(set(words))  # 입력받은 문자열에서 중복값을 제거

count = []
for x in total :
    cnt = words.count(x)
    count.append(cnt)  # count 숫자를 리스트에 append

if count.count(max(count)) > 1 : 
    print('?')
else :
    max = count.index(max(count))  # count 숫자 최대값 인덱스(위치)
    print(total[max])
