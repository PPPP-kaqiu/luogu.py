#first we should judge the palindromic number
#the palindromic number must have odd bits
#we need a function to judge the prume number
#warning:this example may TLE
def judgeprime(number):
    'judge the number if the prime number'
    if number%6!=1 and number%6!=5:
            return False
    for i in range(5,int(pow(number,1/2))+1,6):
        if number%i==0 or number%(i+2)==0:
            return False
    return True
def judgepalindromic(number):
    'judge if the number is the palindromic'
    medium=list(str(number))
    for i in range(len(medium)//2):
        if medium[i]!=medium[len(medium)-1-i]:
            return False
    return True
def judgebit(number):
    if len(list(str(number)))%2==0 and number!=11:
        return False
    return True
begin,end=map(int,input().split())
end=min(9999999,end)
array=[]
if begin%2==0:
    if judgebit(begin)==True:
        if judgepalindromic(begin)==True:
            if judgeprime(begin)==True:
                    print(i)
    for i in range(begin+1,end+1,2):
        if judgebit(i)==False:
            continue
        if judgepalindromic(i)==False:
            continue
        if judgeprime(i)==False:
            continue
        array.append(i)
else:
    for i in range(begin,end+1,2):
        if judgebit(i)==False:
            continue
        if judgepalindromic(i)==False:
            continue
        if judgeprime(i)==False:
            continue
        array.append(i)
for i in array:
    print(i)