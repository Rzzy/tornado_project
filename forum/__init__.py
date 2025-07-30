from tornado.web import Application
import peewee_async
from config import sql_setings, settings

database = peewee_async.MySQLDatabase(**sql_setings)
manager = peewee_async.Manager(database)

from router import handlers
def creat_app():
  app = Application(handlers, **settings)
  app.listen(8000)