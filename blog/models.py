from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):

    author = 'the user'
    content = 'thecontent'
    published = 'published date'
    created = 'created date'

