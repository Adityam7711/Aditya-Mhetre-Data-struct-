#bouble sort and selection sort 
#hihest sal display 
# selection sort 


#================================== Bouble sort =================================

# arr = [6, 6, 8, 4, 1, 2 ]

# n = len(arr)

# for i in range (n-1):
#     for j in range(n-1-i):
#         if arr[j]> arr[j+1]:
#             arr[j],arr[j+1] = arr[j +1],arr[j]
# print(arr)

#====================================== Selection sort ============================


# arr = [22, 43, 14, 28, 35,]
# n = len(arr)

# for i in range(n - 1):
#     mid_index = i 
    
#     # Find the smallest element 
#     for j in range (i + 1 ,n ):
        
#         if arr[j]< arr[mid_index]:
#             min_index = j 
            
#     #swap 
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)


# Display highest sal using bouble sort 

sal = []
n = int(input("enter the number of staff"))
for i in range(n):
    sal.append(int(input("Enter the sal of staff ")))


for i in range(n-1 ):
    for j in range(n-1 - i):
        if sal[j]> sal[j+1]:
            sal[j],sal[j+1]= sal[j+1],sal[j]
print(sal)


#Display highest sal using selection sort 
sallary = []
num = int(input('enter the number of staff'))
for i in range(num):
    sallary.append(int(input("Enter the sal of staff ")))
count = len(sallary)   

for i in range (count - 1 ):
    min_index = i
    
    for j in range(i + 1,count ):
        if sallary[j] < sallary[min_index]:
            min_index = j
            
    sallary[i], sallary[min_index]= sallary[min_index],sallary[i]
    
print(sallary)
         


















