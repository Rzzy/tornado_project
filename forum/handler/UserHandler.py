from uuid import uuid4
from forum.wtform import UserForm
from forum import manager
from forum.models import UserModel
from forum.utils.ResMessageMap import get_dict_msg
from forum.handler.BaseHandler import BaseHandler
import jwt
from config import jwt_secret
from forum.decorators import login_require

class AddUserHandler(BaseHandler):
  async def post(self):
    # 创建一个相应的对象
    res_data = {}
    # 接受请求的参数并封装到From对象中
    user_form = UserForm(self.request.arguments)
    if user_form.validate():
      # 保存数据， 验证用户名是否存在
      email = user_form.email.data
      try:
        # 从数据库中查询数据
        exist_user = await manager.get(UserModel, email = email)
        if exist_user:
          res_data = get_dict_msg(500, msg='user is exist')
      except Exception:
        # 不存在，则创建用户
        user_form.id.data = uuid4()
        await manager.create(UserModel, **user_form.data)
        res_data = get_dict_msg(200)
    else:
      err_data = {}
      for err in user_form.errors:
        err_data[err] = user_form.errors[err][0]
      res_data = get_dict_msg(500, data = err_data)
    self.finish(res_data)
'''
class GetUserHandler(BaseHandler):
  async def get(self):
    res_data = {}
    # 获取token
    token = self.request.headers.get('token')
    if token:
      # 解析token
      paylaod = jwt.decode(token, jwt_secret, algorithms='HS256')
      # 通过email 查询数据
      if paylaod:
        email = paylaod.get('email')
        try:
          usr = await manager.get(UserModel, email = email)
          res_data = get_dict_msg(200, data = usr.to_dict())
        except Exception as e:
          print(e)
          res_data = get_dict_msg(500, data = 'token 解析失败')
      else: 
        res_data = get_dict_msg(401)
    else:
      res_data = get_dict_msg(401)

    self.finish(res_data)
  '''
class GetUserHandler(BaseHandler):
  @login_require
  async def get(self):
    res_data = {}
    # 获取token
    id = self._user_id
    # 通过email 查询数据
    try:
      usr = await manager.get(UserModel, id = id)
      res_data = get_dict_msg(200, data = usr.to_dict())
    except Exception as e:
      print(e)
      res_data = get_dict_msg(500, data = 'get user failed')

    self.finish(res_data)