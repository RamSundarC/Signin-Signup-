# SIGIN / SIGNUP 
The code helps the user to sigin and signup to their accounts.However it manages the user details in mysql database by the python input.

Firstly,it allows user to Signup :
	If the user wants to signup and it asks some information about user such as to  enter
1. User_id
2. Password
3. Name of the user
4. Date of Birth
5. Location
6. Security Question

<i>Then it pushes the user data in mysql database table named profile table and then it pushes to credentials table by using a trigger.</i>


Secondly,it allows user to Signin:
	Otherwise the user wants to signin their account and it ask the user to enter his/her 
1.User_id
2.Password
 
If the user entered correct data and it allows to user to signin his/her accounts

Else if if the user forgot the password it helps the user to rechange the password by asking the user to enter correct details of his/her security question when creating the account.if the user enter correct details he/she can change the password in Credentials table and it will be automatically updated in profile table by a trigger called updater.
