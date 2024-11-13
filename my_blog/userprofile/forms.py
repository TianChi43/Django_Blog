from django import forms

# 导入User模型
from django.contrib.auth.models import User


# 登录表单
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
