from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .forms import Find_user, Reset_password, Edit_group, User_create
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import  QrCod
import random, string
# from .forms import Repo_url
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from django.views.generic import DetailView
from django.conf import settings
import qrcode.image.svg
from io import BytesIO
import datetime


def random_digit():
    return ''.join(random.choice('1234567890') for _ in range(4)) #random.choice("123456789")


from django.contrib.auth import get_user_model
User = get_user_model()


class ProfileDetailView(generic.DetailView):
    model = QrCod
    def get_object(self, queryset=None):
        qr = QrCod.objects.get(qr_hash=self.kwargs.get("qr_id"))
        print(qr.qr_cod_id)
        user = User.objects.get(id=qr.qr_cod_id)
        print('user', user)

        I = user.last_name
        F = user.first_name
        O = user.patronymic
        qr.fio = F[0].ljust(len(F)-1, '*') + ' ' + I[0].ljust(len(I)-1, '*') + ' ' + O[0].ljust(len(O)-1, '*')
        print(user.passport_serial, user.passport_number)
        qr.PASPORT = str(user.passport_serial)[0:2] + '** ***' + str(user.passport_number)[3:6]
        dt_now = datetime.datetime.now() + datetime.timedelta(days=60)
        qr.valid_date = dt_now #user.date_joined
        qr.date_of_birth = user.date_of_birth
        return qr


# @login_required
# def qr_gen(request):
#     pr = User.objects.get(id=request.user.id)

#     qr = QrCod.objects.get(qr_cod=pr)
#     qr_id = qr.qr_hash
#     context = {}
#     factory = qrcode.image.svg.SvgImage

#     ur_url = 'https://gosuslugi-covid.info/certs/' + qr_id
#     img = qrcode.make(ur_url, image_factory=factory, box_size=40)
#     stream = BytesIO()
#     img.save(stream)
#     context["svg"] = stream.getvalue().decode()

#     return render(request, "certs/qr.html", context=context)

