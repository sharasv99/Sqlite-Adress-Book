import sqlite3
con=sqlite3.connect('Data.db')

def insertData(name,age,city):
    qry="insert into Data (Name,Age,City) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("User Details Added")

def updateData(name,age,city,id):
    qry="update Data set NAME=?,AGE=?,CITY=? where id=?;"
    con.execute(qry,(name,age,city,id))
    con.commit()
    print("User Details Updated")

def deleteData(id):
    qry="delete from Data where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("User Details Deleted")

def selectData():
    qry="select * from Data"
    result=con.execute(qry)
    for row in result:
        print(row)

print("""
1.Insert
2.Update
3.Delete
4.Select
""")

ch=1
while ch==1:
    c=int(input("Select Your Choice : "))
    if(c==1):
        print("Add New Record")
        name=input("Enter Name : ")
        age=input("Enter Age : ")
        city=input("Enter City : ")
        insertData(name,age,city)
    elif (c==2):
        print("Edit A Record")
        id=input("Enter ID : ")
        name=input("Enter Name : ")
        age=input("Enter Age : ")
        city=input("Enter City : ")
        updateData(name,age,city,id)
    elif (c==3):
        print("Delete A Record")
        id=input("Enter ID : ")
        deleteData(id)
    elif (c==4):
        print("All Records")
        selectData()
    else:
        print("Invalid Selection")
    ch=int(input("To Continue Press 1: "))
