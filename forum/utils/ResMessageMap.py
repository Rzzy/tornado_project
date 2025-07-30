message_map = {
  200: 'success',
  500: 'error',
  401: 'error'
}

def get_dict_msg(code = 200, data = None, msg = None):
  return {
    'code': code,
    'data': data if data else [],
    'msg': msg if msg else message_map[code]
  }