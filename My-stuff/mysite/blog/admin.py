from django.contrib import admin

from blog.models import *


from django import forms
from django.contrib import admin
from django.utils.timezone import now

from .models import Post


admin.site.register(Post)
