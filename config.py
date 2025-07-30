
sql_setings = {
  'database': 'forum',
  'host': 'localhost',
  'port': 3306,
  'user': 'root',
  'password': '1234'
}

import os
# 设置静态路径
base_path = os.path.abspath(os.path.dirname(__file__))
settings = {
  'static_path': os.path.join(base_path, 'static'),
  'static_url_prefix': '/static/',
  'debug': True
}

jwt_secret = 'wewqnewe,qmwbewebwkb'