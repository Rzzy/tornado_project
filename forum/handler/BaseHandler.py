from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
  def set_default_headers(self) -> None:
    self.set_header('Access-Control-Allow-Origin', '*')

class IndexHandler(RequestHandler):
  async def get(self):
    self.write('hello tornado')
    