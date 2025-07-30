from forum.wtform import LoginUserForm
from forum import manager
from forum.models import UserModel
from forum.utils.ResMessageMap import get_dict_msg
from forum.handler.BaseHandler import BaseHandler
import jwt # 地址： jwe.io
from config import jwt_secret

class LoginHandler(BaseHandler):
  async def post(self):
    res_data = {}
    log_info = LoginUserForm(self.request.arguments)
    if log_info.validate():
      try:
        usr = await manager.get(UserModel, email = log_info.email.data, password = log_info.password.data)
        # 生成一个token 返回给前端
        payload = {
          'email': log_info.email.data
        }
        token = jwt.encode(payload, jwt_secret, algorithm='HS256') # 要加密的数据， 要加密的密码， 加密算法
        res_data = get_dict_msg(200, data = {
          'result': 'login success',
          'token' : token
        })
      except Exception:
        res_data = get_dict_msg(401, data = ' no permission')
    else: 
      err_data = {}
      for err in log_info.errors:
        err_data[err] = log_info.errors[err][0]
      res_data = get_dict_msg(401, data = err_data)
    self.finish(res_data)