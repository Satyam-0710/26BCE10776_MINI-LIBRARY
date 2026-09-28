from LIBRARY_MODULE import *

print("WELCOME to MINI library!!!\n\n")


Book_no = ["B01","B02","B03","B04","B05","B06","B07","B08"]

book_name  = ["Python","Python","Calculus","Calculus","EVS","EVS","ETC","ETC"]


print("\n1.Display all Books\n2.Search for Books\n3.Borrow books from the library")
print("4.Return issued books\n5.Add new books\n6.Exit library database \n")

n = int(input("\nEnter the \"number corresponding to your choice\": "))
n-=1          #To match list indexing

while n != 5 :

    if n == 0:
        displaybooks(Book_no,book_name)

    elif n == 1 :
        searchbooks(book_name)

    elif n == 2:
        borrowbooks(Book_no,book_name)

    elif n == 3:
        returnbooks(Book_no,book_name)

    elif n == 4:
        addbooks(Book_no,book_name)
    
    else:
        print("\nInvalid input. Please enter choice in between 1 to 6 only.\n")

    n = input("Enter \"CONTINUE\" to continue accessing the library: ")

    if n == "CONTINUE" :
        n = looping()

    else:
        print("-"*50)
        break
    
print("\nThanks for using!!!")