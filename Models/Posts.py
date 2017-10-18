import pymongo, bcrypt
from pymongo import MongoClient

class Posts:
  def __init__(self):
    self.client = MongoClient()
    self.db = self.client.codewizard
    self.users = self.db.users
    self.posts = self.db.posts
    
  def insert_post(self, data):
    print("P: DOING INSERT POST")
    inserted = self.posts.insert({'username': data.username, 'content':data.content})
    print(inserted)
    return True

  def get_all_posts(self):
    all_posts = self.posts.find()
    new_posts = []
    for post in all_posts:
      post['user'] = self.users.find_one({'username': post["username"]})
      new_posts.append(post)
    
    return new_posts