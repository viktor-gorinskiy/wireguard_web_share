from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# from .forms import LoginForm
# from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserEditForm
from .models import CustomUser
# from status.models import Profile
# from django.contrib.auth.models import User
# import qrcode
# import qrcode.image.svg
# from io import BytesIO
import random
import string


def random_digit():
    return ''.join(random.choice('1234567890') for _ in range(4)) #random.choice("123456789")


def index(request):
    return render(request, 'main.html',)


def register(request):
    if request.user.is_authenticated:
        print('Уже зареган')
        return render(request, 'users/error.html')
    else:
        if request.method == 'POST':
            print(request.POST)
            user_form = RegisterForm(request.POST)
            if user_form.is_valid():
                # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
                print('new_user ==>', new_user)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
                # Save the User object
                new_user.save()
                # print('new_user', new_user)
                # print('new_user.email', new_user.email)
                return render(request, 'registration/register_done.html', {'new_user': new_user})
        else:
            user_form = RegisterForm()
        return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        print(request.POST)

        user_form = UserEditForm(instance=request.user, data=request.POST)
        print(user_form)

        if user_form.is_valid():
            print('user_form!!!', user_form.cleaned_data)

            # qr_serial = random_digit() + ' ' + random_digit() + ' ' + random_digit() + ' ' + random_digit()
            # qr_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(30))
            # valid_date = '2022-01-27'

            user = CustomUser.objects.get(id=request.user.id)
            # user.patronymic = user_form.cleaned_data['patronymic']
            user.date_of_birth = user_form.cleaned_data['date_of_birth']

            user_form.save()
            # return render(request, 'registration/register_done.html', {'new_user': new_user})

    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'users/edit.html', {'user_form': user_form,})
