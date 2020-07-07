sum = 0
a = 3
b = 5
i = 1
while (a*i < 1000):
    sum += a*i
    i = i+1

i = 1
while (b*i < 1000):
    if ((b*i)%a != 0):
        sum += b*i
    i = i+1

print(sum)
