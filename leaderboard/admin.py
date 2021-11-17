from django.contrib import admin
from .models import Customer
from .models import Matche
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry
from admin_interface.models import Theme


admin.site.register(Customer)
admin.site.register(Matche)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Theme)


LogEntry.objects.all().delete()


