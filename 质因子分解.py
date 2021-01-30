
#the resolve of the prime factor
#we define two array
#the first array store the prime number
#the second array store the number of prime
def judge(number):
    'judge if the target is the prime number'
    for i in prime:
        if number%i==0:
            return False
    return True

def resolve(number):
    'resolve the number into prime number'
    for j in range(0,len(prime)):
        #resolve
        while number!=1:
            if number%prime[j]==0:
                count[j]+=1
                number/=int(prime[j])
            else:
                break

prime=[2]
count=[0]
target=int(input())

for i in range(3,target+1):
    #complete the array of the prime number
    tag=judge(i)#judge the prime
    if tag==True:
        prime.append(i)
        count.append(0)

for i in range(2,target+1):
    resolve(i)

for i in range(0,len(prime)):
    print(prime[i],count[i])