from django.contrib import admin

from .models import Users, Words, UserWords

admin.site.register([Users, Words, UserWords])