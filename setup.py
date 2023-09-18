from setuptools import setup, find_packages

setup(
    name='ylibrary',
    version='v.0.1.0',
    author='Fathimah Yasmin',
    author_email='fathimahyasmin21@gmail.com',
    description='Library Borrowing & Data Management Application',
    packages=find_packages(where='src'),
    python_requires='>=3.9, <4',
    url='https://github.com/fathimahyasmin/CRUD_LibraryBorrowingSystem',
)