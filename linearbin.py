
list = [100, 102 ,103 ,106,108,109,110,111,113,114]
custId = int(input("enter the cust Id:"))


#=================================== Liner sarch =======================================

# for i in range(len(list)):
#     if(list[i]==custId):
#         print("id matched")
#         print(list[i])
#     else:
#         print("id not matched ")
#     i+=1

#=================================== Binary sarch =======================================

low = list[0]
high = len(list) - 1
#mid = (low + high)/ 2 
found = False

while low <= high:
    mid = (low + high)//2
    
    
    if list[mid]==custId:
            print("Id found",list[mid])
            break
    elif(custId < list[mid] ):
            high = mid -1
            
    else:
            low = mid + 1 
    
else:
    print("element not found:")

# lst = [100, 102, 103, 106, 108, 109, 110, 111, 113, 114]

# custId = int(input("Enter the cust Id: "))

# low = 0
# high = len(lst) - 1

# found = False

# while low <= high:
#     mid = (low + high) // 2

#     if lst[mid] == custId:
#         print("Id found:", lst[mid])
#         found = True
#         break

#     elif custId < lst[mid]:
#         high = mid - 1

#     else:
#         low = mid + 1

# if not found:
#     print("Element not found")













