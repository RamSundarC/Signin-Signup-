import pandas as pd
import mysql.connector
import functions
# importing the required modules


db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="@ArchOS123",
    database="BOTBASE"
)
# connecting to the database

cursor=db.cursor() 
# creating cursor object

print("\t \t \t \t \t \t WELCOME")
# welcome message



open1=int(input("Select options:\n\t1.Signup\n\t2.Signin\t"))
# asking user to signup or signin

if open1==1:
# if user is new then he/she has to signup
    print("You're a new user and please fill the particulars")

    functions.importer()
    # calling the function to import the data



elif open1==2:
# if user is already registered then he/she has to signin
    print("You're a Registered user")

    functions.checker()
    # calling the function to check the data





