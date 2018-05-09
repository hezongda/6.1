import numpy as np

k=0 #记录循环次数
tr=0    #用于循环二分法
t=0     #用于当解不在范围内时循环输入

func=input('请输入函数：')
def f(x):
    return eval(func)

while t==0:
    a=float(input('请输入a:'))
    b=float(input('请输入b:'))
    er=float(input('请输入精确度er:'))

    while tr==0:
        if f(a)*f(b)>0:
            print('解不在范围内，请重试')
            print( )
            break

        elif f(a)*f(b)==0:
            if f(a)==0:
                print('方程的解是：',a)
                print('循环次数：',k)
                tr=1
                t=1
            else:
                print('方程的解是：',b)
                print('循环次数：', k)
                tr = 1
                t=1

        else:
            m=0.5*(a+b)

            if np.abs(b-a)<er:
                print('方程的解是：',m)
                print('循环次数：', k)
                tr = 1
                t=1
            else:
                if f(a)*f(m)>0:
                    a=m
                else:
                    b=m
                k=k+1
