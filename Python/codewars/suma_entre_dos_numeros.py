a = 0
b = -1
acum = 0

if a <= b:
    for i in range(a,b+1):
        acum += i
else:
    for i in range(b,a+1):
        acum += i
print(acum)