"""
利用字母可以组成一些美丽的图形，下面给出了一个例子：

ABCDEFG

BABCDEF

CBABCDE

DCBABCD

EDCBABC

这是一个5行7列的图形，请找出这个图形的规律，并输出一个n行m列的图形
"""
n,m = map(int,input().split())
ls = []
for i in range(65,91):
    ls.append(chr(i))
str1 = "".join(ls)
for j in range(n):
    if j < m:
        print(str1[j::-1],end = "")
        print(str1[1:(m-j)])
    else:
        print(str1[j:(j-m):-1])
