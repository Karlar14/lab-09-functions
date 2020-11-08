def factorial(n): # this is a function
    total = 1    # variable of total equals one

    for i in range(1,n+1):
        total = total * (i)
        # print("Current i is " + i)
        # print("Current value of tool is " + total)

    return total

usernum = int(input("number please: "))


print(usernum + " ! is " + factorial(usernum))
