from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register([Contact, BlogCategory, BlogTag, Blog, BlogReply, Review, Media])
