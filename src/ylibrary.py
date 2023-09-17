# IMPORT DEPENDENCIES
# --------------------------------------------------------------------------
from datetime import datetime, timedelta
import pyinputplus as pyip
import tabulate
import csv
import os

# LOGIN & REGISTRATION
# --------------------------------------------------------------------------

def registration(memberdbase):
    while True: 
        name = pyip.inputStr('Enter your username: ')
        name = name.lower()
        email = pyip.inputEmail('Enter your email address: ')
        email = email.lower()
        phone_num = pyip.inputInt('Enter your phone number: ')
        hold = 0

        duplicate = False 

        for data in memberdbase.values():
            if data[1].lower() == name:
                print('This username is already registered.')
                duplicate = True
                break
            elif data[2] == phone_num:
                print('This phone number is already registered.')
                duplicate = True
                break
            elif data[3].lower() == email: 
                print('This email is already registered')
                duplicate = True

        clear_screen()

        if not duplicate:
            member_id = generate_id(memberdbase, code='M')
            true_pass = '123456' + member_id[1:]

            data = [member_id, name.capitalize(), phone_num, email, hold]
            memberdbase.update({f'{member_id}': data})
            with open('ylibrary\member.csv', mode='a', newline='') as file:
                    writer = csv.writer(file, delimiter = ';')
                    writer.writerow(data)

            clear_screen()
            print('CONGRATULATION!')
            print('Your registration is successful')
            print(f'>>>  Your member ID is : {member_id}')
            print(f'>>>  Your password is : {true_pass}')

            break

def generate_id(memberdbase, code):

    max_id = 0

    for i in memberdbase.keys():
        num_part = i[1:]
        if num_part.isdigit():
            max_id = max(max_id, int(num_part))
    
    new_id = f'{code.capitalize()}{max_id + 1}'
    return new_id

def admin_login():
    while True:
        true_pass = 'abcdefg'
        password = pyip.inputPassword("Enter your password: ").lower()
        if true_pass.lower() != password:
            print('Invalid password')
            print('Please try again')
        else: 
            identity = 'admin'
            id = None
            return identity, id
        
def member_login(memberdbase):
    while True:
        found = False

        member_id = pyip.inputStr("Enter your member ID: ").lower()

        password = pyip.inputPassword("Enter your password: ")
        true_pass = '123456' + member_id[1:]

        for member in memberdbase.values():
            if member[0].lower() == member_id and password == true_pass:
                found = True

        if not found:
            print('Invalid member ID or password')
            print('Please try again')
        else:
            identity = 'member'
            id = member_id.capitalize()
            return identity, id

def log_or_reg(memberdbase):
    while True:
        print('-------- WELCOME TO Y-LIBRARY --------')
        log_or_reg = pyip.inputStr('''  
To login, please choose the menu: 
                                
1. Login as member
2. Login as admin
3. New member registration
                               
Enter the number: ''')
        
        if log_or_reg == '1':
            identity, id = member_login(memberdbase)
            return identity, id
        elif log_or_reg == '2':
            identity, id = admin_login()
            return identity, id
        elif log_or_reg == '3':
            registration(memberdbase)

# CLEAR SCREEN 
# --------------------------------------------------------------------------
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def stay():
    back = pyip.inputYesNo(prompt="\nEnter 'y' or 'yes' to go back to the main menu: ")
    if back == 'yes':
        clear_screen()
    else:
        print("Invalid input. Please enter 'y' or 'yes'.")

# SHOW DATA & ALL DATABASE
# --------------------------------------------------------------------------

def show(database):
    attributes = []
    header = database['column']

    for id, attribute in database.items():
        if id == 'column':
            pass
        else:
            attributes.append(attribute)
    
    print(tabulate.tabulate(attributes, header, tablefmt='grid'))

def partial_show(part, database):
    header = database['column']
    print('Search result: ')
    print(tabulate.tabulate(part, header, tablefmt='grid'))
    
# MAIN MENUS
# --------------------------------------------------------------------------
# Search()
# --------------------------------------------------------------------------
def search(database):
    while True:
        print('---------- BOOK SEARCH ----------')
        searchOpts = pyip.inputInt(lessThan=7, prompt='''
Let's find your book!. 
Here's some searching options:
                           
1.  By Title
2.  By Author
3.  By Category
4.  By ISBN               
5.  See all books
6.  Back to main menu                         
                           
Enter the menu number: ''')
        
        found = False
        attributes = []
        
        if searchOpts == 1:
            title = pyip.inputStr('Enter the title: ').lower()

            for id, attribute in database.items():
                if title == database[id][1].lower():
                    attributes.append(attribute)
                    found = True
    
            if not found:
                print(f'Sorry, {title.title()} was not found in our database')
            else:
                partial_show(attributes, database)
                stay()

        elif searchOpts == 2:
            author = pyip.inputStr('Enter the author name: ').lower()

            for id, attribute in database.items():
                if author == database[id][2].lower():
                    attributes.append(attribute)
                    found = True
    
            if not found:
                print(f'Sorry, {author.title()} was not found in our database')
            else:
                partial_show(attributes, database)
                stay()
        elif searchOpts == 3:
            category = pyip.inputStr('Enter the category: ').lower()

            for id, attribute in database.items():
                if category == database[id][3].lower():
                    attributes.append(attribute)
                    found = True
    
            if not found:
                print(f'Sorry, {category} was not found in our database')
            else:
                partial_show(attributes, database)
                stay()
        elif searchOpts == 4:
            isbn = pyip.inputStr('Enter the ISBN number: ')

            for id, attribute in database.items():
                if isbn == database[id][4]:
                    attributes.append(attribute)
                    found = True
    
            if not found:
                print(f'Sorry, {isbn} was not found in our database')
            else:
                partial_show(attributes, database)
        elif searchOpts == 5:
            show(database)
            stay()
        elif searchOpts == 6:
            break

# Add()
# --------------------------------------------------------------------------

def add(database, identity):

    if identity != 'admin':
        print('This menu is for admin only.')
        return

    while True:
        print('-------- INPUT DATABASE ---------')
        print('''
Choose the menu:
1. Add Book
2. Exit
        ''')
        addOpts = pyip.inputInt('Enter the number: ')
        
        if addOpts == 1:
            book_id = generate_id(database, code='B')
            #book_id = pyip.inputStr('Enter book ID: ')
            title = pyip.inputStr('Enter title: ')
            authors = pyip.inputStr('Enter authors: ')
            category = pyip.inputStr('Enter category: ')
            isbn = pyip.inputInt(prompt='Enter ISBN number (13 digit): ')
            publisher = pyip.inputStr('Enter publisher: ')
            stock = pyip.inputInt('Enter stock: ')

            data = [book_id, title.title(), authors.title(), category, isbn, publisher.title(), stock]

            save = pyip.inputYesNo("Do you want to save this data? (yes/no): ")

            if save == 'yes':
                with open('ylibrary\libdata.csv', mode='a', newline='\n') as file:
                    writer = csv.writer(file, delimiter = ';')
                    writer.writerow(data)
                print("The input was successful.")
            else:
                print("The input was not saved.")
        
        elif addOpts == 2:
            break

# Update()
# --------------------------------------------------------------------------

def update(database, identity):
    
    if identity != 'admin':
        print('This menu is for admin only.')
        return 
    
    while True:
        
        print('-------- UPDATE DATABASE --------')
        print('''
Choose the menu:
1. Update Book Data
2. Exit
        ''')
        sub_choice = pyip.inputInt('Enter the number: ')
        if sub_choice == 1:
            while True: 
                book_id = pyip.inputStr('\nEnter the book ID to update: ').capitalize()
                
                if book_id not in database:
                    print(f'Book ID {book_id} not found in database.')
                else: 
                    data = database[book_id]
                    print(tabulate.tabulate([data], headers=database['column'], tablefmt='grid'))
                    break
            
            while True:
                confirm = pyip.inputYesNo("Do you want to continue update? (yes/no): ")

                if confirm == 'no':
                    break
                else: 
                    print('''
Select which data you want to update: 
1. Title
2. Author
3. Category
4. ISBN
5. Publisher
6. Stock
        ''')
                updateOpts = pyip.inputStr('Enter the number: ')
        
                if updateOpts == '1':
                    newTitle = pyip.inputStr('\nEnter new title: ')
                    data[1] = newTitle.title()
                elif updateOpts == '2':
                    newAuthor = pyip.inputStr('\nEnter new Author: ')
                    data[2] = newAuthor.title()
                elif updateOpts == '3':
                    newCategory = pyip.inputStr('\nEnter new Category: ')
                    data[3] = newCategory
                elif updateOpts == '4':
                    newIsbn = pyip.inputInt('\nEnter new ISBN (13 digits): ')
                    data[4] = newIsbn
                elif updateOpts == '5':
                    newPub = pyip.inputStr('\nEnter new Publisher: ')
                    data[5] = newPub.title()
                elif updateOpts == '6':
                    newStock = pyip.inputInt('\nEnter new stock: ')
                    data[6] = newStock
        
                confirm_save = pyip.inputYesNo('Do you want to save this update? (yes/no): ')

                if confirm_save == 'yes':
                    with open('ylibrary\libdata.csv', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(database.values())
                    print('Change saved successfully')
                    print(tabulate.tabulate([data], headers=database['column'], tablefmt='grid'))
                    break
                else: 
                    print("The input was not saved.")
                    break
        elif sub_choice == 2:
            break

# Delete()
# --------------------------------------------------------------------------

def delete(database, identity):

    if identity != 'admin':
        print('This menu is for admin only.')
        return
    
    while True:
        clear_screen()
        print('-------- DELETE DATABASE --------')
        print('''
Choose the menu:
1. Delete Book Data
2. Exit
        ''')
        sub_choice = pyip.inputInt('Enter the number: ')
        
        if sub_choice == 1:
            while True: 
                book_id = pyip.inputStr('\nEnter the book ID you want to delete: ').capitalize()
            
                if book_id not in database:
                    print(f'Book ID {book_id} not found in database.')
                else: 
                    data = database[book_id]
                    print(tabulate.tabulate([data], headers=database['column'], tablefmt='grid'))
                    break

            while True:
                confirm = pyip.inputYesNo("Do you want to continue delete? (yes/no): ")

                if confirm == 'yes': 
                    del database[book_id]
                    print('Data successfully deleted')

                    with open('ylibrary\libdata.csv', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(database.values())
                    break

                else:
                    print("Deletion cancelled. No changes were made.")
                    break
       
        elif sub_choice == 2:
            break

# Borrow()
# --------------------------------------------------------------------------

def borrow(database, memberdbase, borrowdb, identity, user_id):

    if identity != 'member':
        print('This menu is for member only.')
        return
    
    while True:
        print('-------- BOOK BORROWING --------')
        print('''
Choose the menu:
1. Borrow Books
2. Read Borrowing Policy
3. Check Borrowing History
4. Exit''')
        sub_choice = pyip.inputInt('Enter the number: ')

        #clear_screen()
             
        if sub_choice == 1:
            print('\nBorrowing Quota Status: ')
            print('-----------------------------')
            # check hold
            hold = memberdbase[user_id][4]
            remain = 3 - hold
    
            if remain == 0:
                print('\nSorry, you\'ve reached the borrowing limit')
                print('You can borrow another book next time!')
                break
            else:
                print(f'\nYour available borrowing quota is {remain}')

            #clear_screen()

            while True: 
                book_id = pyip.inputStr('\nEnter the book ID you want to borrow: ').capitalize()
                if book_id not in database:
                    print(f'\nBook ID {book_id} not found in database.')
                else: 
                    #cek stock
                    data = database[book_id]
                    stock = data[6]
                    if stock == 0:
                        print('\nSorry, your book isn\'t available')
                        print(f'The book stock is {stock}')

                    else: 
                        print('\nYey! Your book is available')
                        print(f'The remaining stock is {stock}')

                        confirm_save = pyip.inputYesNo('\nDo you want to continue borrowing? (yes/no)') 
                        if confirm_save == 'yes':
                            data[6] -= 1
                            memberdbase[user_id][4] += 1

                            with open('ylibrary\libdata.csv', 'w', newline='') as file:
                                writer = csv.writer(file, delimiter=';')
                                writer.writerows(database.values())

                            with open('ylibrary\member.csv', 'w', newline='') as file:
                                writer = csv.writer(file, delimiter=';')
                                writer.writerows(memberdbase.values())

                            borrow_date = datetime.now()
                            return_date = borrow_date + timedelta(days=7)

                            entry_num = generate_id(borrowdb, code='C')

                            cart = [entry_num, user_id, book_id, borrow_date, return_date]

                            with open('ylibrary\databorrow.csv', 'a', newline='') as file:
                                writer = csv.writer(file, delimiter = ';')
                                writer.writerow(cart)
                            
                            print('Yey! Borrowing successful!')
                            print('Check the borrowing status in "Check Borrowing History" menu')
                            stay()
                            break
                        else: 
                            break
        
        elif sub_choice == 2:
            clear_screen()
            with open('ylibrary\libpolicy.txt', 'r') as file:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                
                content = file.read()
                print(content)
                
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            stay()
        elif sub_choice == 3:
            print('-------- BORROWING HISTORY --------')
            
            data = []
            header = ['Member ID', 'Name', 'Book Title', 'Borrow Date', 'Return Date']

            for j in borrowdb.values():
                if j[1] == user_id:
                    name = memberdbase[j[1]][1]
                    title = database[j[2]][1]
                    borrowdate = j[3][:10]
                    returndate = j[4][:10]
                    compile = [user_id, name, title, borrowdate, returndate]
                    data.append(compile)

            print(tabulate.tabulate(data, header, tablefmt='grid'))
            stay()

        elif sub_choice == 4:
            break     

# search_member()
# --------------------------------------------------------------------------
def search_member(memberdbase):
    while True: 
        print('---------- MEMBER DATA SEARCH ----------')
        searchOpts = pyip.inputInt(lessThan=7, prompt='''
Search options:                                                          
1.  Search Member ID
2.  Show All
3.  Exit                         
                           
Enter the menu number: ''')
        
        found = False
        attributes = []
        
        if searchOpts == 1:
            user_id = pyip.inputStr('Enter the member id: ').lower()

            for id, attribute in memberdbase.items():
                if user_id == memberdbase[id][0].lower():
                    attributes.append(attribute)
                    found = True
    
            if not found:
                print(f'{user_id.capitalize()} was not found in database')
            else:
                partial_show(attributes, memberdbase)
                stay()
        elif searchOpts == 2:
            show(memberdbase)
            stay()
        elif searchOpts == 3:
            break
        
# update_member()
# --------------------------------------------------------------------------
def update_member(memberdbase):

    while True:
        print('-------- UPDATE MEMBER DATA --------')
        print('''
Choose the menu:
1. Update Member Data
2. Exit
        ''')
        sub_choice = pyip.inputInt('Enter the number: ')
        if sub_choice == 1:
            while True: 
                member_id = pyip.inputStr('\nEnter the member ID to update: ').capitalize()
                
                if member_id not in memberdbase:
                    print(f'Member ID {member_id} not found in database.')
                else: 
                    data = memberdbase[member_id]
                    print(tabulate.tabulate([data], headers=memberdbase['column'], tablefmt='grid'))
                    break
            
            while True:
                confirm = pyip.inputYesNo("Do you want to continue update? (yes/no): ")

                if confirm == 'no':
                    break
                else: 
                    print('''
Select which data you want to update: 
1. Name
2. Phone Number
3. Email
4. Hold
        ''')
                updateOpts = pyip.inputStr('Enter the number: ')
        
                if updateOpts == '1':
                    newName = pyip.inputStr('\nEnter new name: ')
                    data[1] = newName.title()
                elif updateOpts == '2':
                    newPhone = pyip.inputInt('\nEnter new phone number: ')
                    data[2] = newPhone
                elif updateOpts == '3':
                    newEmail = pyip.inputEmail('\nEnter new email: ')
                    data[3] = newEmail
                elif updateOpts == '4':
                    newHold = pyip.inputInt('\nEnter new hold status: ')
                    data[4] = newHold
        
                confirm_save = pyip.inputYesNo('Do you want to save this update? (yes/no): ')

                if confirm_save == 'yes':
                    with open('ylibrary\member.csv', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(memberdbase.values())
                    print('Change saved successfully')
                    print(tabulate.tabulate([data], headers=memberdbase['column'], tablefmt='grid'))
                    break
                else: 
                    print("The input was not saved.")
                    break
        elif sub_choice == 2:
            break

# delete_member()
# --------------------------------------------------------------------------
def delete_member(memberdbase):
    while True:
        clear_screen()
        print('-------- DELETE MEMBER DATA --------')
        print('''
Choose the menu:
1. Delete Book Data
2. Exit
        ''')
        sub_choice = pyip.inputInt('Enter the number: ')
        
        if sub_choice == 1:
            while True: 
                member_id = pyip.inputStr('\nEnter the member ID you want to delete: ').capitalize()
            
                if member_id not in memberdbase:
                    print(f'Member ID {member_id} not found in database.')
                else: 
                    data = memberdbase[member_id]
                    print(tabulate.tabulate([data], headers=memberdbase['column'], tablefmt='grid'))
                    break

            while True:
                confirm = pyip.inputYesNo("Do you want to continue delete? (yes/no): ")

                if confirm == 'yes': 
                    del memberdbase[member_id]
                    print('Data successfully deleted')

                    with open('ylibrary\member.csv', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerows(memberdbase.values())
                    break

                else:
                    print("Deletion cancelled. No changes were made.")
                    break
       
        elif sub_choice == 2:
            break

# DATABASE MANAGEMENT
# --------------------------------------------------------------------------
def database_management(database, memberdbase, identity):

    if identity != 'admin':
        print('This menu is for admin only.')
        return
    
    while True: 
        print('-------- DATABASE MANAGEMENT SYSTEM --------')
        print('''          
Menu:
1. Add book data
2. Update book data
3. Delete book data
4. Search member data
5. Update member data
6. Delete member data             
7. Exit
        ''')
        
        choice = pyip.inputStr('Enter the number: ')

        if choice == '1':
            add(database)
        elif choice == '2':
            update(database)
        elif choice == '3':
            delete(database)
        elif choice == '4':
            search_member(memberdbase)
        elif choice == '5':
            update_member(memberdbase)
        elif choice == '6':
            delete_member(memberdbase)
        elif choice == '7':
            break