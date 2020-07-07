sum = 0
f = 1
f_old = 1

while(f<4000000):
    if(f%2==0):
        sum += f
    f = f + f_old 
    f_old = f - f_old

print(sum)   
