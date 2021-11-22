def fibo(x):

    list123=[0,1]
    for i in range(2,x):
        a=list123[-1]
        b=list123[-2]
        c=a+b
        list123.append(c)
    print(list123)
    
    # just try with big number, It is a art, be safe.
