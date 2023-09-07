import traceback

def calculator():
    
    # Get dog age
    d_age = input("Input dog years: ")

    try:
            age = float(d_age)
            if age >= 0:
                dog_age=age
                if 0<=age<=1:
                    age=age*15
                elif 1.1<=age<=2.0:
                    age=age*12
                elif 2.1<=age<=3.0:
                    age=age*9.3
                elif 3.1<=age<=4.0:
                    age = age*8
                elif 4.1<=age<=5:
                    age= age*7.2
                else :
                    age= (36) + (age-5)*7
                human_age=round(age,2)
                print ("The given dog age "+ str(dog_age)+" is "+ str(human_age)+ " in human years. ")
            else:
                print ("Age cannot be negative")
            

    except:
        print(d_age, " is an invalid age.")
       
    
calculator() 
