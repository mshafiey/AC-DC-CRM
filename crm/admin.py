from django.contrib import admin
from .models import Customer
from .models import CustomerCall

admin.site.register(Customer)

admin.site.register(CustomerCall)
