def isPalindrome(x):
    temp = x
    reverseX = 0
    while(temp>0):
        reverseX = (reverseX * 10) + (temp % 10)
        temp = int(temp / 10)

    if (reverseX == x):
        return True
    else:
        return False

n = 999999
while(True):
    # print("Number : ", n)
    if(isPalindrome(n)):
        for i in range(999,100,-1):
            if(n % i == 0):
                j = n / i
                if(i>99 and j>99 and i<1000 and j<1000):
                    print(n)
                    exit()

    n -= 1
