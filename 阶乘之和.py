#in spite of the demand for high precision
#the data in test don't reach the limit of python far from
#thus we don't need other means to solve the problem
def factorial(number):
    'calculate the factorial of number'
    if number==1:
        return 1
    return number*factorial(number-1)
number=int(input())
sum=0
for i in range(1,number+1):
    sum+=factorial(i)
print(sum)