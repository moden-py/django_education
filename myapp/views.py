from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from myapp.models import MAIN_USER_ID


def index(request):
    try:
        me = User.objects.get(id=MAIN_USER_ID)
    except User.DoesNotExist:
        presenter_data = None
    else:
        presenter_data = (me.first_name,
                          me.last_name,
                          me.email)
    context = {'presenter_data': presenter_data}
    return render(request, 'myapp/index.html', context)


class UserEditView(UpdateView):
    model = User

