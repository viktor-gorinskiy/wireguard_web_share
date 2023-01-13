from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


################################################################

class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        # fields = ['email', 'first_name', 'last_name', 'patronymic', 'date_of_birth', 'passport_serial', 'passport_number',]
        fields = ['email',]

    def clean_email(self):
        print('\nclean_email\n')
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        print('email ==>', email)
        qs = CustomUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Такой email уже зарегистрирован.")
        return email



    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        print('cleaned_data ==>', cleaned_data)
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")

        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")


        # passport_serial = cleaned_data.get("passport_serial")
        # passport_number = cleaned_data.get("passport_number")

        # print('passport_serial', type(passport_serial), passport_serial)
        # print('passport_number', type(passport_number), passport_number)

        # if passport_serial is None:
        #     print("Серия в паспорте не может быть пустой")
        #     self.add_error("passport_serial", "Серия в паспорте не может быть пустой")
        # if passport_number is None:
        #     print("Номер в паспорте не может быть пустой")
        #     self.add_error("passport_number", "Номер в паспорте не может быть пустой")


        # if not isinstance(passport_serial, int):
        #     print('Только числа')
        #     self.add_error("passport_serial", "Только цифры")

        # if not isinstance(passport_number, int):
        #     print('Только числа')
        #     self.add_error("passport_number", "Только цифры")

        # if len(str(passport_serial)) != 4:
        #     print(' !=4 ')
        #     self.add_error("passport_serial", "Должно быть 4 цифры")


        # if len(str(passport_number)) != 6:
        #     print('!=6')
        #     self.add_error("passport_number", "Должно быть 6 цифр")
        # #

        return cleaned_data


class UserEditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        # fields = ('email',)
#         # fields = ('first_name', 'last_name', 'date_of_birth', 'patronymic', 'passport_serial', 'passport_number',)
        fields = ('first_name', 'last_name', 'date_of_birth',)
