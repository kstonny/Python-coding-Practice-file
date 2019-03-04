import sqlite3

Mybook = sqlite3.connect('libdata.db')
nm = input("Please enter the book you want: ")
sql = "SELECT * from library WHERE title='"+nm+"';"

curlib=Mybook.cursor()
curlib.execute(sql)
result = list(curlib.fetchone())
print("Yes this book exist",result)


noOfCopies =int(input("Enter the no of copies"))

totalPrice = int(result[3])


print(totalPrice*noOfCopies)