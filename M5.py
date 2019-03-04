import sqlite3

Mybook=sqlite3.connect('libdata.db')
curlib=Mybook.cursor()
curlib.execute('''CREATE TABLE library (BookId INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT(25) NOT NULL, author TEXT (25), price INTEGER);''')

for x in range(3):
    ttl=input("Please enter title of book ")
    aut = input("Please enter author of book ")
    prc = input("Please enter the price of book ")

    data = "INSERT INTO library (title,author,price) VALUES('"+ttl+"','"+aut+"','"+prc+"');"

    try:
        curlib=Mybook.cursor()
        curlib.execute(data)
        Mybook.commit()
        print("Data has been registered")
    except:
        print("Error")
        Mybook.rollback()

Mybook.close()