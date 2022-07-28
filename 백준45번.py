# 2941번


arr= ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()

for i in arr:

    b = b.replace(i, '*')

print(len(b))