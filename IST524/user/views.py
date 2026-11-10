
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import RegisterCaptchaForm



def register_view(request):
    if request.method == "POST":

        captcha_form = RegisterCaptchaForm(request.POST)

        if not captcha_form.is_valid():
            return render(request, 'users/register.html', {
                'error': 'Неправильная CAPTCHA!',
                'captcha_form': captcha_form
            })

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'users/register.html', {
                'error': 'Пароли не совпадают!',
                'captcha_form': RegisterCaptchaForm()
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {
                'error': 'Такой логин уже существует!',
                'captcha_form': RegisterCaptchaForm()
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {
                'error': 'Этот email уже используется!',
                'captcha_form': RegisterCaptchaForm()
            })

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password1
        )

        Profile.objects.create(
            user=user,
            phone=phone,
            birth_date=birth_date
        )

        login(request, user)

        return redirect('/profile/')

    captcha_form = RegisterCaptchaForm()

    return render(request, 'users/register.html', {
        'captcha_form': captcha_form
    })


def auth_login_view(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/profile/')

        return render(request, 'users/login.html', {
            'error': 'Неправильный логин или пароль!'
        })

    return render(request, 'users/login.html')


@login_required(login_url='/login/')
def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'users/profile.html', {
        'user': request.user,
        'profile': request.user.profile
    })
