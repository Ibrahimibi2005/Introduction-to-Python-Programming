num_list=[]
i=0
playing = True

while (playing ==True):
    num = int(input("Enter an int: "))
    if(num==-1):
        playing =False
    else:
        num_list.append(num)
        i+=1
num_sum = 0
for num in num_list:
    num_sum+=num
avg = num_sum/i

print ("avg: ",avg)
# reverse
string ='pasta'
rev =''

for j in range(len(string)-1,-1,-1):


x=[1,2,3,4]
print (x[4])
