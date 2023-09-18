def isNarcissistic(x):
    sum=0
    l=str(x)
    n=str(x)
    for i in l:
        result=int(i)**len(l)
        sum=sum+result
    if (sum==int(x)):
        return True
    return False
def isComposite(x):
    if x==1:
        return False
    for i in range(2,x):
        if x % i==0:
            return True
       
    return False
isComposite(1)
def isPerfect(x):
    sum=0
    for i in range(1,x):
        if x % i==0:
            sum=sum + i  
    if(sum==x):
        return True
    else:
        return False
isPerfect(33550335)
def getFactors(x):
    l=[]
    for i in range(1,x+1):
        if x % i==0:
            l.append(i)
    return l
def isPrime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x % i==0:
            return False
       
    return True    

def isAbundant(x):
    sum=0
    for i in range(1,x):
        if x % i==0:
            sum=sum + i  
    if(sum>x):
        return True
    else:
        return False
isAbundant(12)
def isTriangular(x):
    if (x==1):
        return True
    for i in range(1,x):
        n=i*(i + 1) / 2
        if(n==x):
            return True
        
    return False
isTriangular(2) 
isNarcissistic(1)
def main():

    playing = True
    while playing == True:

        num_input = input('Give me a number from 1 to 10000.  Type -1 to exit. ')

        try:
            num = int(num_input)

            if (num == -1):
                playing = False
                continue

            if (num <= 0 or num > 10000):
                continue

            factors = getFactors(num)
            print("The factors of", num, "are", factors)

            if isPrime(num):
                print(str(num) + ' is prime')
            if isComposite(num):
                print(str(num) + ' is composite')
            if isPerfect(num):
                print(str(num) + ' is perfect')
            if isAbundant(num):
                print(str(num) + ' is abundant')
            if isTriangular(num):
                print(str(num) + ' is triangular')
            if isNarcissistic(num):
                print(str(num) + ' is narcissistic')

        except ValueError:
            print('Sorry, the input is not an int.  Please try again.')
            
#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()
