# Wrong Approach

num = 20
i = num
while(True):
    for x in range(num, 1, -1):
        if(i % x == 0):
            print(i, x)
            if(x == 2):
                print(i)
                exit()
        else:
            break

    i += num
