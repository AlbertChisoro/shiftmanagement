from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Leave)
admin.site.register(Shifts)
admin.site.register(EmployeeShiftRecords)
