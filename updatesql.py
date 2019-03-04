import sqlite3

Myschool = sqlite3.connect('schooltest.db')

nm = input("Please enter the name: ")
sql = "SELECT * from student WHERE name= '"+nm+"';"

curschool = Myschool.cursor()
curschool.execute(sql)
record=curschool.fetchone()
print(record)

m = float(input("Enter new marks: "))
sql= "UPDATE student SET marks='"+str(m)+"' WHERE name='"+nm+"';"

try:
    curschool.execute(sql)
    Myschool.commit()
    print("Record has been updated")

except:
    print("Error Updating Record")
    Myschool.rollback()