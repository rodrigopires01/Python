import mysql.connector


def query():

    text = "SELECT A.ProductID, A.ProductName, C.SupplierID, C.CompanyName, B.CategoryID, B.CategoryName FROM Products A JOIN Categories B using(CategoryID)JOIN Suppliers C using(SupplierID)ORDER BY A.ProductID;"
    return text


if __name__ == '__main__':

    mydb = mysql.connector.connect(
        host="northwind.c34l1rcgahc1.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Passw0rd",
        database="northwind"
    )

    mycursor = mydb.cursor()
    mycursor.execute(query())
    myresult = mycursor.fetchall()

    for x in myresult:
        print(f'{x[0]: <3} {x[1]: <35} {x[2]: <3} {x[3]: <40} {x[4]: <3} {x[5]: <10}')
