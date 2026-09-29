# Mini Library Management System

A Mini Library Management System built using Python. This project is a small library where users can manage a collection of books through a simple list of choices.

## Features

- Search for books in the library
- Issue available books
- Return issued books
- Add new books to the library
- Check whether a book is available or already issued

## Technologies Used

- Python 3

## How to access the code

1. Clone the repository:

```bash
git clone https://github.com/Satyam-0710/26BCE10776_MINI-LIBRARY.git
```

2. Navigate to the project folder:

```bash
cd 26BCE10776_MINI-LIBRARY

```

3. Run the main program:

```bash
python mini_library.py
```

> **Note:** Keep `mini_library.py` and `library_module.py` in the same folder, as the main program imports functions from `libray_module.py`.

## Project Structure

```
Mini-Library/
│
├── mini_library.py      # Main program
├── library_module.py    # Contains the library functions
├── README.md
└── statement.md
```

## Future Improvements

- Save library data to SQL
- Add user authentication (Via university ID card)
- Include due dates and fine calculation
- Develop a better user interface
- Different list of options for librarian and students

## Learning Outcomes

Through this project, I practiced:

- Working with Python modules
- Creating reusable functions with def
- Using lists to manage data
- Implementing conditional statements and loops


## How to run 
- When running the code , the user will get multiple options , such as Displaying all books , Searching for books , etc.
- Its recommended that the user goes through the option one by one .
- When choosing 1 , the interpreter will show all pre-defined books in the library i.e. 8 books .
- Next , the user will be asked to enter "Continue", after entering "Continue" ,the user should choose 2 .
>**Note:** The user will be asked to enter CONTINUE after each iteration. 
-  That will allow user to search the availability of books , to make sure if the books are in the library or are issued to someone else .
> **Note:** To do that , user should enter the book name that was previously displayed when the user chose 1 .
- Accordingly , user can use 3 and 4 to borrow and return new books from the library , based on its Book ID .
- Now , 5 is an option meant for the librarian to add new books into the library . Choosing 5 , user will be asked how many new books are to be added and the Book ID and Book name of the new books to be added.
- This whole process is in a looping statement (while) and hence option 6 lets the user exit the library and a "Thanks for using" Message is displayed.

## Author

**Satyam Mishra**
