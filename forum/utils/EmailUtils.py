import zmail

def send_email(from_email:str, to_email: str, password: str,subject: str, context_text: str) -> None:
  # 创建服务
  server = zmail.server(from_email, password)
  # 发邮件
  server.send_mail(to_email, { 'subject': subject, 'context_text': context_text})