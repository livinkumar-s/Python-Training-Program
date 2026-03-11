import mysql.connector

# mySQLConnector=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="12345",
#     database="dummy"
# )

# print("Successfully connected !")
# cursor=mySQLConnector.cursor()

#Creating Table

# query="CREATE TABLE userData (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) unique, email VARCHAR(255) unique, password VARCHAR(255))"

# cursor.execute(query)

#CRUD
# try:
#     query="INSERT INTO userData (name, email, password) VALUES (%s, %s, %s)"

#     cursor.execute(query,("Allu Arjun","aa@gmail.com","1234554321"))
#     mySQLConnector.commit()

#     print("User added!")
# except mysql.connector.errors.IntegrityError:
#     print("User already !Exist")


# Read
# query="SELECT * FROM userData"
# cursor.execute(query)
# res=cursor.fetchall()
# res=cursor.fetchone()
# print(res)

# query="UPDATE userData SET password=%s WHERE id=%s"

# cursor.execute(query,("123",4))
# mySQLConnector.commit()


class Auth:
    def __init__(self):
        self.connectionObj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="dummy"
)
        self.cursor=self.connectionObj.cursor()

    
    def signUp(self,userName,password,email):
        try:
            query="INSERT INTO userdata (name,email,password) VALUE (%s,%s,%s)"
            self.cursor.execute(query,(userName,email,password))
            self.connectionObj.commit()
            print("SignedUp Successfully!")
        except mysql.connector.errors.IntegrityError:
            print("User already Exist!")
    def login(self,email,password):
        query="SELECT * from userdata where email=%s"
        self.cursor.execute(query,(email,))
        currentUser=self.cursor.fetchone()
        if currentUser:
            if currentUser[3]==password:
                print("Logged in Successfully!")
            else:
                print("Invalid Password!")
        else:
            print("User does not exist")

auth1=Auth()

auth1.login("aaa@gmail.com","1234")