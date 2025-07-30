from wtforms_tornado import Form
from wtforms.fields import StringField, HiddenField
from wtforms.validators import DataRequired, Length

class UserForm(Form):
  id = HiddenField()
  email = StringField('邮箱', validators=[DataRequired(message='emial is need')])
  nick_name = StringField('昵称', validators=[Length(min=2, max=10, message='length:2~10')])
  password = StringField('密码', validators=[Length(min=2, max=10, message='length:2~10')])
  signature = StringField('签名')
  pic = StringField('头像')


class LoginUserForm(Form):
  id = HiddenField()
  email = StringField('邮箱', validators=[DataRequired(message='emial is need')])
  nick_name = StringField('昵称')
  password = StringField('密码', validators=[Length(min=2, max=10, message='length:2~10')])
  signature = StringField('签名')
  pic = StringField('头像')