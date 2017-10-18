import pymongo
from pymongo import MongoClient
import bcrypt

class LoginModel:
  def __init__(self):
    self.client = MongoClient()
    self.db = self.client.codewizard
    self.col_users = self.db.users
    
  def check_user(self, data): 
    print("LM-check_user")
    user = self.col_users.find_one({"username": data.username})
    if user:
      print("User Found")
      if bcrypt.checkpw(data.password.encode(), user["password"]):
        print("Correct Password")
        return user   
    return False