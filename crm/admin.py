from django.contrib import admin
from .models import Customer
from .models import CustomerCall
from .models import Director, Manager, Employee, TechnicalHelp

admin.site.register(Customer)

admin.site.register(CustomerCall)

admin.site.register(Director)

admin.site.register(Manager)

admin.site.register(Employee)

admin.site.register(TechnicalHelp)
