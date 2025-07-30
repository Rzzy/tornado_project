from peewee import *
from forum import database
from datetime import datetime

class BaseModel(Model):
  create_time = DateTimeField(default = datetime.now, verbose_name = '创建时间')
  def to_dict(self) -> dict:
    r = {}
    for k in self.__data__.keys():
      # 判断属性是否是 create_time
      if k == 'create_time':
        r[k] = str(getattr(self, k))
      else:
        r[k] = getattr(self, k)
    return r
  class Meta:
    database = database

class UserModel(BaseModel):
  id = CharField(primary_key = True)
  email = CharField(max_length=32, verbose_name = '邮箱')
  nick_name = CharField(max_length=32, verbose_name = '昵称', null = True)
  password = CharField(max_length=32, verbose_name = '密码')
  signature = CharField(max_length=32, verbose_name = '签名', null = True)
  pic = CharField(max_length=32, verbose_name = '头像',  null = True)
  status = IntegerField(verbose_name='账号状态', default=1)

  class Meta:
    table_name = 't_user'