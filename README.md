# Library Borrowing System
Capstone Project Modul 1 JCDS Purwadhika

The Library Borrowing System is a CRUD-based program that facilitates the borrowing process for both library members and administrators. It provides functionalities such as searching for books, registering borrowings, checking borrowing history, managing databases, and more.

## Features
### For Members:
1. **Search Book:**
   - Allows members to search for books using various criteria like book ID, title, ISBN, category, etc.
2. **Borrow:**
   - Enables members to borrow books by providing the book ID. The program automatically updates their remaining borrowing quota and provides feedback on the borrowing process.
3. **Borrow Policy:**
   - Provides access to the library's borrowing policies for members to familiarize themselves with the rules.
4. **Check Borrowing History:**
   - Allows members to view the books they've borrowed and check their due dates for return.

### For Administrators:
1. **Search:**
   - Allows administrators to search for books, members, and view borrowing histories.
2. **Add Data:**
   - Enables administrators to add new books to the respective databases.
3. **Update Data:**
   - Provides the ability to update existing book or member information.
4. **Delete Data:**
   - Allows administrators to remove books or members from the databases.
5. **Check Member Borrowing History:**
   - Provides access to view the borrowing history of all or specific members.

## Dependencies
```PyInputPlus==0.2.12```
```tabulate==0.9.0```
```datetime==3.11.5```

## Usage
1. Decide your role as either a member or an administrator.
2. If you're a member, log in with your credentials. If not, register to receive a member ID and password.
3. In the main menu:
   - Use the Search Book option for both roles.
   - Use Borrow as a member to borrow books.
   - Use Database Management as an administrator to manage databases.

## Project Organization
```
├── README.md          <- The top-level README for developers using this project.
│
├── data               <- book database, member database, borrowing database
|            
├── src                <- Source code for use in this project.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
```

## Contributing
If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Create a pull request.

