import firebase_admin
import json
from firebase_admin import db



cred_obj = firebase_admin.credentials.Certificate('hackathon-6c0c9-firebase-adminsdk-mvfav-92e3c52dc8.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://hackathon-6c0c9-default-rtdb.firebaseio.com/"
	})

ref = db.reference("/")





with open("userdata.json", "r") as f:
	file_contents = json.load(f)
ref.update(file_contents)



