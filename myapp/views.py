from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    try:
        me = User.objects.get(username='moden')
    except User.DoesNotExist:
        presenter_data = None
    else:
        presenter_data = (me.first_name,
                          me.last_name,
                          me.email)
    context = {'presenter_data': presenter_data}
    return render(request, 'myapp/index.html', context)
