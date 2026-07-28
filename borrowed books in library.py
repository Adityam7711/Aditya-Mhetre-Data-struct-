member = int(input ("enter the number of members "))
books_barrow= [] * member
total_no = 0 
zero_byer = 0 
most_freq_byer = 0
# Adding nomber of book barrowed by member to an list 
for i in range (member):
    print("Enter number of books borrowed by member ",i + 1)
    num = int(input("Enter:" ))
    books_barrow.append(num)
    i += 1
print("total books barrow by member :",books_barrow)

#Total of boks barrow 
for i in books_barrow:
    total_no = total_no + i 
    i += 1 
print("total_books :",total_no)
# 1 calculating the avg of the book
avg_no =int( total_no/ member ) 
print( "the average no of book :",avg_no)

# calculating highest and lowest book borrow by member 
# highest = max(books_barrow)
# print("the highest book barrow by member:", highest)
# minimum  = min(books_barrow)
# print("the min book barrow by member:", minimum)
 
# calculating zero book member 
highest= books_barrow[0]
lowest = books_barrow[0]
for i in range (1,member):
    if books_barrow[i] > highest:
        highest = books_barrow[i]
    if books_barrow[i]< lowest:
        lowest= books_barrow[i]



for i in books_barrow:
    if(books_barrow[num] == 0):
        zero_byer+=1  
print("member of member who buy zero book ",zero_byer)

# for i in books_barrow:
#     most_freq_byer = 0 
#     for j in books_barrow:
#         if (books_barrow[i]== books_barrow[j] ):
#             most_freq_byer+=1 
# print("most frequent byer :", most_freq_byer)

#calc most frequent buyer 
for i in range(len(books_barrow)):
    count = 0 
    for j in range(len(books_barrow)):
        if books_barrow[i]==books_barrow[j]:
            count+=1 
    # print("the most frequent byer book is :",count,"times ")
print ("the most  frequent books buyers :", count )
