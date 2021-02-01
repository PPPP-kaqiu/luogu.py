#station
#demands:
#in the first station,the number of getting on the bus is a
#in the second station,the number of getting on or the of  us equal
#in the other stations,the number of getting on the bus is equal to the sum of front two stations
#while the number of getting off the bus is equal to the number of getting on the last station

#we have four input:
#the number of stations is 'n'
#in the first station,the number of getting on the bus is 'a'
#in the last station,the number of getting off the bus is 'm'(the bus is empty)
#test 'x' station

#we assume the number of getting on the bus in the first station is x
#we assume the number of getting on the bus in the second station is y
#this question is similimar to the Fabonacci
#we use the recursion to simulate the process
def coefficientx(number):
    if number==1 or number==2:
        return 1
    if number==3:
        return 2
    return coefficientx(number-1)+coefficientx(number-2)-1

def coefficienty(number):
    if number<=3:
        return 0
    return coefficienty(number-1)+coefficienty(number-2)+1
a,n,m,x=map(int,input().split())
y=(m-coefficientx(n-1)*a)//coefficienty(n-1)
print(coefficientx(x)*a+coefficienty(x)*y)