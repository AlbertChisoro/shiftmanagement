from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *
import random
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate, login
from .models import Employee


WEEKS = (
    ('W1','WEEK1'),
    ('W2','WEEK2'),
    ('W3','WEEk3'),
    ('W4','WEEK4'),
   
)

MONTHS=(
   ('01','JANUARY'),
    ('02','FEBRUARY'),
    ('03','MARCH'),
    ('04','APRIL'),
    ('05','MAY'),
    ('06','JUNE'),
    ('07','JULY'),
    ('08','AUGUST'),
    ('09','SEPTEMBER'),
    ('10','OCTOBER'),
    ('11','NOVEMBER'),
    ('12','DECEMBER'),
)

def employees(request):
    if request.method=='GET':
        employees = Employee.objects.all()
        template = loader.get_template('employee/employee.html')

        context = {
            'employees': employees,
        }
        return HttpResponse(template.render(context, request))
def postEmployees(request):
    if request.method=='GET':
        employee = EmployeeForm()
        context = {'employees': employee}
        return render(request, 'employee/postemployee.html', context)

    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
    return redirect('employees')


def departments(request):
    if request.method=="GET":
        departments=Department.objects.all()
        template = loader.get_template('employee/departments.html')
        form=DepartmentForm()
        context = {
            'form':form,
            'departments':departments
        }
        return HttpResponse(template.render(context, request))
 


def postDepartments(request):
    if request.method=='GET':
        departments = DepartmentForm()
        context = {'departments': departments}
        return render(request, 'employee/postdepartment.html', context)

    if request.method=='POST':
        form=DepartmentForm(request.POST)
        if form.is_valid:
            form.save()
    return redirect('departments')

def leaves(request):
    if request.method=="GET":
        leaves=Leave.objects.all()
        template = loader.get_template('employee/leaves.html')
        form=LeaveForm()
        context = {
            'leaves': leaves,
            'form':form
        }
        return HttpResponse(template.render(context, request))



def makeShifts(request):
    if request.method=="GET":
        employee=sorted(Employee.objects.order_by('?'), key=lambda x: random.random())

        for week in WEEKS:

            for emp in employee:
                shifts=sorted(Shifts.objects.order_by('?'), key=lambda x: random.random())
                for shift in shifts:
                    EmployeeShiftRecords.objects.create(
                        employee=emp.firstname,
                        shift=shift.name,
                        week=week,
                        month=datetime.now().month
                    )
                    shifts.remove(shift)
        # EmployeeShiftRecords.objects.all().delete()
   
    data = [['ID','FIRSTNAME', 'SHIFT', 'DATEALLOCATED', 'WEEK', 'MONTH']]
    employeeshifts=EmployeeShiftRecords.objects.values_list()

    employeeshiftdata=[]
    for ems in employeeshifts:
        employeeshiftdata.append(ems)

    for emp in employeeshiftdata:
        data.append(emp)
    
    simple_table(data)
        
    


def simple_table(data):
	spacing=1 
	pdf = FPDF()
	pdf.set_font("Arial", size=10)
	pdf.add_page()
    # pdf.cell(pdf.font_size, 0.0, 'Demographic data', align='C')
	col_width = pdf.w / 5.5
	row_height = pdf.font_size
	for row in data:
	    for item in row:
	        pdf.cell(col_width, row_height*spacing,str(item), border=1)
	    pdf.ln(row_height*spacing)

	pdf.output('employeeshifts.pdf')
	return data

def home(request):
    return render(request, 'employee/homepage.html')

def register(request):
    if request.method=="GET":
        form=UserCreateForm()
        context={
            'user':form
        }
        return render(request, 'employee/register.html',context)
    elif request.method=="POST":
        form=UserCreateForm(request.POST)
        if form.is_valid:
            form.save()
            
        return redirect('home')

def employeeshifts(request):
    if request.method=="GET":
        employeeshifts=EmployeeShiftRecords.objects.all()
        context={
            'employeerecords':employeeshifts
        }
    return render(request, 'employee/employeeshiftrecords.html', context)

def shiftrecords(request):
    if request.method=="GET":
        shiftrecords=Shifts.objects.all()
        context={
            'shifts':shiftrecords
        }
        return render(request, 'employee/shiftrecords.html', context)


def postShifts(request):
    if request.method=='GET':
        shifts = ShiftsForm()
        context = {'shifts': shifts}
        return render(request, 'employee/postShifts.html', context)
    elif request.method=="POST":
        form=ShiftsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('shiftrecords')
        return redirect('home')

def logout(request):
    auth_logout(request)
    return redirect('home')
 


def loginuser(request):
    if request.method=="GET":
        return render(request, 'employee/login.html')
    elif request.method=="POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('home')
            return redirect('login')
def deleteemployee(request,pk):
    employee=Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('employees')

def deleteshift(request,pk):
    shift=Shifts.objects.get(pk=pk)
    shift.delete()
    return redirect('shifts')

def delete(request,pk):
    department=Department.objects.get(pk=pk)
    department.delete()
    return redirect('departments')
