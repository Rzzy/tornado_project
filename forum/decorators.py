import functools
import jwt
from forum.utils.ResMessageMap import get_dict_msg
from config import jwt_secret
from forum import manager
from forum.models import UserModel

def login_require(func):
  @functools.wraps(func)
  async def wrap(self, *arg, **kwargs):
    res = {}
    # 验证用户是否登录
    # 获取token
    token = self.request.headers.get('token')
    if token:
      payload = jwt.decode(token, jwt_secret, algorithms='HS256')
      # 通过email 查询数据
      if payload:
        email = payload.get('email')
        try:
          usr = await manager.get(UserModel, email = email)
          self._user_id = usr.id
          # 登录成功，执行函数
          await func(self,*arg, **kwargs)
        except Exception as e:
          print(e)
          self.finish(get_dict_msg(401, data = {
            'result': 'no login info'
          }))
      else: 
        self.finish(get_dict_msg(401, data = {
          'result': 'no login info'
        }))
    else: 
      res = get_dict_msg(401, data = {
        'result': 'no login info'
      })
      self.finish(res)
  return wrap  
