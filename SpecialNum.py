# 153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。 编程求所有满足这种条件的三位十进制数
for i in range(100,1000):
    sum = 0
    for j in str(i):
        sum = sum + int(j) ** 3
    if i == sum:
        print(i)
      
# 1221是一个非常特殊的数，它从左边读和从右边读是一样的，编程求所有这样的四位十进制数
for i in range(1000,10000):
    if str(i) == str(i)[::-1]:
        print(i)
      
# 123321是一个非常特殊的数，它从左边读和从右边读是一样的。输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
n = int(input())
for i in range(10000,1000000):
    if str(i) == str(i)[::-1]:
        sum=0
        for j in str(i):
            sum = sum + int(j)
        if sum == n:
            print(i,end = "\n")
