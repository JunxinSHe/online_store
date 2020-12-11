from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, HiddenField, validators

class LoginForm(Form):
    '''渲染用户登陆HTML表单 '''
    userid = StringField('Username：', [validators.DataRequired('Must have username')])
    password = PasswordField('Password：',[validators.DataRequired('Must have password')])

class CustomerRegForm(Form):
    ''' 渲染客户注册HTML表单'''
    userid = StringField('Username：', [validators.DataRequired('Must enter username')])
    name = StringField('Customer Name：', [validators.DataRequired('Must enter customer name')])
    password = PasswordField('Password：', [validators.DataRequired('Must have password')])
    password2 = PasswordField('Enter password again：', [validators.EqualTo('password', message='password must be the same')])
    # 验证日期的正则表达式 YYYY-MM-DD YY-MM-DD
    reg_date = r'^((((19|20)(([02468][048])|([13579][26]))-02-29))|((20[0-9][0-9])|(19[0-9][0-9]))-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))$'
    birthday = StringField('Date of Birth：', [validators.Regexp(reg_date, message='Invalid date')])
    address = StringField('Address：')
    phone = StringField('Mobile：')