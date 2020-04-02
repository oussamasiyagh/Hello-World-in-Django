from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'gender', 'info', 'phone')
    list_editable = ('info',)
    list_per_page = 1
    search_fields = ('name', 'email', 'gender', 'info', 'phone')
    list_filter = ('gender',)


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
