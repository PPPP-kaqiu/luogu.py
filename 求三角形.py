
#output the target matrix and triangle matrix
scale=int(input())
for i in range(1,pow(scale,2)+1):
    print('%02d'% i,end='')
    if i%scale==0:
        print('')
print('')
row=1
tag=True
count=scale*(scale+1)//2
for i in range(1,count+1):
    if tag==True:
        print("  "*(scale-row),end='')
        tag=False
        lable=0

    print('%02d'% i,end='')
    lable+=1

    if lable==row:
        print('')
        tag=True
        row+=1