from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'info', 'phone')


admin.site.register(Contact)
admin.site.unregister(Group)
