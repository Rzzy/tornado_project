from forum.handler import BaseHandler, UserHandler, LoginHandler
handlers = [
  ('/', BaseHandler.IndexHandler),
  ('/user/addUser', UserHandler.AddUserHandler),
  ('/user/getUser', UserHandler.GetUserHandler),
  ('/login', LoginHandler.LoginHandler)
]