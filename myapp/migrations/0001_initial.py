# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password
from myapp.models import MAIN_USER_ID


def setup_admin(apps, schema_editor):
    User = apps.get_model("auth", "User")
    admin = User(
        username='admin',
        email='ad...@admin.com',
        password=make_password('admin'),
        is_superuser=True,
        is_staff=True
    )
    admin.save()

    me = User(
        pk=MAIN_USER_ID,
        username='moden',
        first_name='Denis',
        last_name='Matiychuk',
        email='moden.py@yandex.ru',
        password=make_password('moden'),
        is_staff=True,
    )
    me.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(setup_admin)
    ]
