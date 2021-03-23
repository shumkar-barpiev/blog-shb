from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title','status','slug','author')

admin.site.register(models.Post, PostAdmin)