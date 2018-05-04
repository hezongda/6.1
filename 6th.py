import numpy as np

k=0 #记录循环次数
tr=0    #初始判断值

func=input('请输入函数：')
def f(x):
    return eval(func)

a=float(input('请输入a:'))
b=float(input('请输入b:'))
er=float(input('请输入精确度er:'))

while tr==0:
    if f(a)*f(b)>0:
        print('解不在范围内，请重试')
        break

    elif f(a)*f(b)==0:
        if f(a)==0:
            print(a,k)
            tr=1
        else:
            print(b,k)
            tr = 1

    else:
        m=0.5*(a+b)

        if abs(b-a)<er:
            print(m,k)
            tr = 1
        else:
            if f(a)*f(m)>0:
                a=m
            else:
                b=m
            k=k+1