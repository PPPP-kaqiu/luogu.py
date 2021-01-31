#the refined calculation of the triangle's area
a,b,c=map(float,input().split())
p=(a+b+c)/2
print('%.1f'%(pow(p*(p-a)*(p-b)*(p-c),1/2)))