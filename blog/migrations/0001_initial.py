# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.9.5 on 2016-04-14 09:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
=======
# Generated by Django 1.9.5 on 2016-04-14 09:26
from __future__ import unicode_literals

from django.db import migrations, models
>>>>>>> origin/master


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> origin/master
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
>>>>>>> origin/master
            ],
        ),
    ]
