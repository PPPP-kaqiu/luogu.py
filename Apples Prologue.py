#inspect the surplus of apples
#the first warning:the once is 0,we can eat the whole apples easily
#the second waring:we don't need so much time to eat these apples
apple,once,time=map(int,input().split())
if once==0 or time/once>=apple:
    print(0)
elif time%once==0:
    print('%d'%(apple-time/once))
else:
    print('%d'%(apple-time//once-1))