bill=float(input("Enter meal price: "))
tax=float (input("Enter the sales tax(percentage): "))
Tip=float(input("Enter the tip(percentage): "))

 #calculatong tax:
tax_amount= (bill*tax)/100
total=bill+tax_amount

#calculating tip
tip_amount= (total*Tip)/100
total=total+tip_amount

#rounding total bill by 2 decimal
total= round(total,2)

#print total
print ("The total bill is: $",total,sep=' ')
