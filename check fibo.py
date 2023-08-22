def fibo (x):
    a = 0
    b = 1
    if x==0:  
        return a
    elif x == 1:
        return b
    else:
        for i in range(2 , x+1):
            c = a + b
            a = b
            b = c
        return c
    
fibo_num =[]

def check_fibo(y):
    if y==1 or y==2 or y==3 or y==5:
        x =print(f"{y}  in fibo ")
    else:
        for i in range(0,y):
            fibo_num.append(fibo(i))
        if y in fibo_num:
            x =print(f"{y}  in fibo ")
        else:
            x = print(f"{y} not in fibo")
    return x

y= 8
check_fibo(y)
