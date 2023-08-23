def printnum(num):
    while(num>=0):
        rem=num%10
        num=num/10
        if(rem==7):
            return True
        else:
            return False
        
lis=[135,2,45,24,57,6,765,45,13,65,7,68,98,9764322,47687,87,98,9,98]
print("List of Numbers Ending with 7 is:")
for i in range(len(lis)):
    if(printnum(lis[i])==True):
        print(lis[i],end=" ")