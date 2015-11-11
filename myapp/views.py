from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    me = User.objects.get(username='moden')
    return HttpResponse("{0} {1} {2}".format(me.first_name,
                                             me.last_name,
                                             me.email))
