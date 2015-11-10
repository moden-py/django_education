# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.hashers import make_password


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


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
    migrations.RunPython(setup_admin)
    ]
