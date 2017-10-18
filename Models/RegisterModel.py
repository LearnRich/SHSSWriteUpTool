import pymongo 
from pymongo import MongoClient
import bcrypt

class RegisterModel:
  def __init__(self):
    self.client = MongoClient()
    self.db = self.client.codewizard
    self.users = self.db.users
  
  def insert_user(self, data):
    print("RM: INSERT USER")
    hashpw = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
    id = self.users.insert({
      "username":data.username,
      "name":data.name,
      "password":hashpw,
      "email":data.email
    })
    print("Created uid:", id)
    
  def update_settings(self, data):
    print("RM: UPDATE USER")
    user = self.users.find_one({"username": data.username})
    if user:
      print("User Found")
      if bcrypt.checkpw(data.oldpassword.encode(), user["password"]):
        hashpw = bcrypt.hashpw(data.newpassword.encode(), bcrypt.gensalt())
        update_data = {}
        if len(data.name):
          update_data['name'] = data.name
        if len(data.newpassword):
          update_data['password'] = hashpw
        if len(data.email):
          update_data['email'] = data.email
        print(update_data)
        id = self.users.update({"username":data.username},update_data)
        print("Updated uid:", id)
     