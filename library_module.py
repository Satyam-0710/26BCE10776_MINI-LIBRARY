check = []
check_name = []

def displaybooks(Book_no,book_name):

    print("-"*50)

    for d in Book_no:
        i = Book_no.index(d)
        print(f"Book ID: ", Book_no[i], end=" | ")
        print(f"Book name :",book_name[i])

    print("-"*50)

def searchbooks(book_name):

    print("-"*50)

    print("#If you dont know the Book names or Book IDs , try using DISPLAY first.\n\n")
    f = input("Enter the \"BOOK NAME\" you want to search: ")
    print("-"*50)

    count = book_name.count(f)

    if count == check_name.count(f):
        print("The book is already issued to someone else .")
    else:
        print("This book is available to be issued.")
    print("-"*50)

def borrowbooks(Book_no,book_name):

    print("-"*50)
    print("\nWhich book do you want to borrow?\n") 

    d = input("\nEnter the \"BOOK ID \"of the book you want to borrow: ")
    print("-"*50)

    if d in Book_no and d not in check:
        i = Book_no.index(d)
        print(f"\nBook :\"{book_name[i]}\" is found in the library , and is issued to you.\nPlease return it before 14 days.\n")     
        check.append(d)
        check_name.append(book_name[i])

    elif d in check:
        print("\nSomeone already has this book. Better luck next time.")

    else:
        print("\nSorry, this book does not belong to the library.") 
    print("-"*50)

def returnbooks(Book_no,book_name):

    print("-"*50)
    print("\nWhich book do you want to return?")
    print("-"*50)

    d = input("\nEnter that \"BOOK ID\": ")
    
    if d in Book_no and d in check:
        i = Book_no.index(d)
        check.remove(d)
        check_name.remove(book_name[i])
        print(f"The Book \"{book_name[i]}\" has been returned back to the library successfully.")

    elif d not in Book_no:
        print("\nSorry, this book does not belong to the library.")

    else:
        print("No such book was issued.")
    print("-"*50)

def addbooks(Book_no,book_name):

    k = 1
    print("-"*50)
    number = int(input("\nEnter the \"NUMBER\" of \"NEW BOOKS\" to be added : "))
    print("-"*50)

    while number > 0:
        new_book = input("\nEnter the \"BOOK ID\" of book %d: " %(k))
        
        if new_book in Book_no:
            print("\nThis Book ID already exists. Please enter a unique Book ID.\n")
            continue
            
        Book_no.append(new_book)

        a = input("\nEnter the \"NAME\" of book %d: " % (k))
        book_name.append(a)
        print("-"*50)
        k+=1

        if number == 1 :
            print("\nBook(s) added successfully.\n")
        number -= 1
    k=0

def looping():      #to repeat print the options of the user 

    print("\n",end="",)
    print("-"*50)
    print("What do you want to do next?\n")
    print("1.Display all Books\n2.Search for Books\n3.Borrow books from the library")
    print("4.Return issued books\n5.Add new books  \n6.Exit library database \n")

    n = int(input("\nEnter the \"number corresponding to your new choice\": "))
    n-=1
    print("-"*50)

    return n