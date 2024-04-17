#　给定n个十六进制正整数，输出它们对应的八进制数。
 
bin(x,10)    十进制转二进制
oct(x,10)    十进制转八进制
hex(x,10)    十进制转十六进制
int(x,8/2/16)     其他进制转十进制

n = int(input())
ls1 = []
for it in range(n):
    ls1.append("0x"+input())
ls2 = []
for i in ls1:
    j = oct(int(i,16))
    ls2.append(j)
for t in ls2:
    print(str(t)[2:],end = "\n")
