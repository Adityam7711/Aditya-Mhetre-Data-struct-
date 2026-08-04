
list = [100, 102 ,103 ,106,108,109,110,111,113,114]
custId = int(input("enter the cust Id:"))

found = False
#=================================== Liner sarch =======================================
print("Linear sarch:")
for i in range(len(list)):
    if(list[i]==custId):
        print("id matched")
        print(list[i])
        found = True
        break
if( not found):
    print("id not matched ")
        
    

#=================================== Binary sarch =======================================
print("binary Sarch")
low = 0
high = len(list) - 1
found = False

while low <= high:
    mid = (low + high)//2
    
    
    if list[mid]==custId:
        print("Id found",list[mid])
        found = True
        break
    elif(custId < list[mid]):
        high = mid -1
            
    else:
        low = mid + 1 
    
if not found:
    print("element not found:")















