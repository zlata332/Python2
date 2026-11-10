from django import forms
from captcha.fields import CaptchaField


class RegisterCaptchaForm(forms.Form):
    captcha = CaptchaField()