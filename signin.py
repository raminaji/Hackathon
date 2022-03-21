import firebase_admin
import json
from firebase_admin import db



cred_obj = firebase_admin.credentials.Certificate('hackathon-6c0c9-firebase-adminsdk-mvfav-92e3c52dc8.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://hackathon-6c0c9-default-rtdb.firebaseio.com/"
	})

ref = db.reference("/")
data =ref.get()
users=list(data.keys())

usernames = users
passwords = []
for i in users:
    passwords.append(data[i]["password"])
def signup():
    user_input_u = input("Username: ")
    while user_input_u in usernames:
        print("Error. The Username is already in use.")
        user_input_u = input("Username: ")
    
    user_input_p = input("Password: ")  
    ref.update({user_input_u:{"password":user_input_p}})

def sign_ins():
    print("\nSign in. ")
    user_input_u = input("Username: ")
 
    while user_input_u not in usernames:
        print("Error. The Username is incorrect. Please try again.")
        user_input_u = input("Username: ")
    user_input_p = input("Password: ")
 
 
    for i in range(len(usernames)):
        if user_input_u == usernames[i]:
            while user_input_p != passwords[i]:
                print("Error. The Password is incorrect. Please try again.")
                user_input_p = input("Password: ")
    print("Logged in!")
