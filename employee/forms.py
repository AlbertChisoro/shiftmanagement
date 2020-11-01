from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DepartmentForm(ModelForm):
    
    class Meta:
        model=Department
        fields=['name','description']
class LeaveForm(ModelForm):
    class Meta:
        model=Leave
        fields='__all__'
class ShiftsForm(ModelForm):
    class Meta:
        model=Shifts
        fields='__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['firstname','lastname','email','onleave','department']
class UserCreateForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        



