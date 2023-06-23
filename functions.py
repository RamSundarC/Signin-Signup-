import mysql.connector
import pandas as pd


db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="@ArchOS123",
    database="BOTBASE"
)

cursor=db.cursor()


def importer():
    user_id=input("Create Your User_id:\t") # asking user to create user_id
    password=input("Create Youre Password:\t") # asking user to create password
    name=input("Enter Your Name:\t") # asking user to enter name
    dob=input("Enter Date in Format of YYYY-MM-DD:\t") # asking user to enter date of birth
    location=input("Enter Your Location:\t") # asking user to enter location
    security_question=input("Enter Your Name of Pet Animal:\t") # asking user to enter security question

    dic={"ip1":[user_id],
         "ip2":[password],
         "ip3":[name],
         "ip4":[dob],
         "ip5":[location],
         "ip6":[security_question]} # pushing the data into dictionary
    
    df=pd.DataFrame(dic)

    sql="INSERT INTO PROFILE (user_id,password,name,dob,location,security_question) VALUES (%s,%s,%s,%s,%s,%s)"
    data=(user_id,password,name,dob,location,security_question)

    cursor.execute(sql,data) # pushing the data into the database

    db.commit() # commiting the changes


def checker():
    ip1=(input("Enter User-Id:\t")) # asking user to enter user_id

    l=[] # creating a list
    a=cursor.execute("SELECT User_Id from CREDENTIALS") # selecting the user_id from the database
    users=cursor.fetchall() # fetching the data

    for b in users:    
        l.append(b)   # pushing the data into the list
        

    if (ip1,) in l: # checking the user_id
        print("User_Name Verified Successfully..")
    else:
        print("Denied Access")

    ip2=input("Enter Password:\t") # asking user to enter password

    l1=[] # creating a list
    a1=cursor.execute(f'SELECT Password from CREDENTIALS where User_Id= "{ip1}" ') # selecting the password from the database
    passwords=cursor.fetchone() # fetching the data

    for g in passwords:
        l1.append(g)    # pushing the data into the list

    if (ip2) in l1: # checking the password
        print("Password Verified Successfully")

    else:
        print("Incorrect Credentials")

        ip5=int(input("Press 0 For Forgot Password")) # asking user to enter 0 for forgot password
        
        if ip5==0:
            changer()


def changer():
    ip3=input("Enter Your User_Id:\t") # asking user to enter user_id
    print("Security Question: ")

    sq=input("Enter Your Pet Name:\t") # asking user to enter security question
    
    res=cursor.execute(f'SELECT security_question from PROFILE WHERE User_id="{ip3}" ') # selecting the security question from the database
    ret=cursor.fetchone()[0] # fetching the data
    
    if ret==sq: # checking the security question
        ip4=input("Enter Your New Password:\t") # asking user to enter new password
        print("Password Changed Successfully")
        cursor.execute(f'UPDATE CREDENTIALS SET Password="{ip4}" WHERE User_Id="{ip3}"') # updating the password in the database
      
        
        db.commit() # commiting the changes



















        
        