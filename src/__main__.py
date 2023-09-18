import csv
import pyinputplus as pyip
import ylibrary as ylib

def book_db():
    try: 
        with open('ylibrary\data\libdata.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)
            database = {'column' : header}
            for row in reader:
                book_id, title, author, category, isbn, publisher, stock = row
                database.update({book_id : [book_id, title, author, category, isbn, publisher, int(stock)]})
                pass
    except ValueError as ve:
        print(f'ValueError Occurred : {ve}')
    return database

def member_db():
    try:
        with open('ylibrary\data\member.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)
            memberdbase = {'column' : header}
            for row in reader:
                member_id, name, phone_num, email, hold = row
                memberdbase.update({member_id : [member_id, name, int(phone_num), email, int(hold)]})
                pass
    except ValueError as ve:
        print(f'ValueError occured: {ve}')
    return memberdbase 

def borrow_db():
    try:
        with open('ylibrary\data\databorrow.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            header = next(reader)
            borrowdb = {'column' : header}
            for row in reader:
                no, userID, bookID, borrowDate, returnDate = row
                borrowdb.update({no : [no, userID, bookID, borrowDate, returnDate]})
                pass
    except ValueError as ve:
        print(f'ValueError occured: {ve}')
    return borrowdb 

def main():
    global database, memberdbase, borrowdb
    identity, user_id = ylib.log_or_reg(memberdbase)

    while True:
        ylib.clear_screen()
        print('-------- WELCOME TO Y-LIBRARY --------')
        print('------ let\'s feed your curiosity -----')
        print('''          
Menu:
1. Search Books
2. Borrow book
3. Database Management
4. Exit
        ''')
        
        choice = pyip.inputStr('Enter the number: ')
        if choice == '1':
            ylib.clear_screen()
            ylib.search(database)
        elif choice == '2':
            ylib.clear_screen()
            ylib.borrow(database, memberdbase, borrowdb, identity, user_id)
        elif choice == '3':
            ylib.clear_screen()
            ylib.database_management(database, memberdbase, identity)
        elif choice == '4':
            ylib.clear_screen()
            print('----------------------------------')
            print('\nThank you for visiting Y-Library')
            print('See you next time!')
            print('\n----------------------------------')
            break

if __name__ == "__main__":
    ylib.clear_screen()
    database = book_db()
    memberdbase = member_db()
    borrowdb = borrow_db()
    main()

