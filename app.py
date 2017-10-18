import web
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
  '/', 'Home',
  "/register", "Register", 
  "/postreg", "PostRegistration",
  '/login', 'Login',
  '/check-login', "CheckLogin",
  '/logout', 'Logout',
  '/post-activity', 'PostActivity',
  '/profile', 'Profile',
  '/settings', 'Settings',
  '/update-user', 'UpdateSettings'
)

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore("sessions"),initializer={"user":None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={"session":session_data, "current_user": session_data["user"]})

# *** Classes/Routes ***
# Each class will be a conrtoller for a different route.
class Home:
  def GET(self):
    data = type('obj', (object,), {'username':'richardson_b', 'password':'1234'})
    login = LoginModel.LoginModel()
    isValid = login.check_user(data)
    if isValid:
      session_data['user'] = isValid

    post_model = Posts.Posts()
    posts = post_model.get_all_posts()
      
    return render.Home(posts)
  
class Register:
  def GET(self):
    return render.Register()

class PostRegistration:
  def POST(self):
    print("DOING POST PROCESSING")
    data = web.input()
    reg_model = RegisterModel.RegisterModel()
    reg_model.insert_user(data)
    return data.username

class Login:
  def GET(self):
    return render.Login()
  
class CheckLogin:
  def POST(self):
    print("DOING CHECK LOGIN")
    data = web.input()
    login = LoginModel.LoginModel()
    isValid = login.check_user(data)
    if isValid:
      session_data["user"] = isValid
      return isValid
    return "error"
  
class Logout:
  def GET(self):
    print("DOING LOGOUT")
    session['user'] = None
    session_data['user'] = None
    session.kill()
    return "success"

class PostActivity:
  def POST(self):
    print("DOING POST ACTIVITY")
    data = web.input()
    data.username = session_data['user']['username']
    post_model = Posts.Posts()
    post_model.insert_post(data)    
    return "success"

class Profile:
  def GET(self):
    return render.Profile()

class Settings:
  def GET(self):
    return render.Settings()

class UpdateSettings:
  def POST(self):
    data = web.input()
    data.username = session_data['user']['username']
    update = RegisterModel.RegisterModel()
    update.update_settings(data)
    return "success"
    
if __name__ == "__main__":
  app.run()

  
  
  
  
  
  
  