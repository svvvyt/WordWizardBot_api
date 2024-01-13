from django.contrib import admin

from .models import User, Word, UserWord

admin.site.register([User, Word, UserWord])