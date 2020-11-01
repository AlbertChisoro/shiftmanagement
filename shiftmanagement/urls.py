from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from employee import views

urlpatterns = [
        url(r'post-shiftrecords/',views.postShifts,name="post-shiftrecords"),
    url(r'employeeshiftrecords/',views.employeeshifts,name="employeeshiftrecords"),
    url(r'shiftrecords/',views.shiftrecords,name="shiftrecords"),
        path('deleteemployee/<int:pk>/',views.deleteemployee,name="deleteemployee"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^employees/',views.employees,name='employees'),
    url(r'^departments/',views.departments,name='departments'),
    url(r'^add-departments/',views.postDepartments,name='add-departments'),
    url(r'post-employees/',views.postEmployees,name='post-employees'),
    url(r'post-departments/',views.postDepartments,name="post-departments"),
    url(r'login/',views.login,name="login"),
    url(r'register/',views.register,name="register"),
    url(r'^logout', views.logout, name='logout'),
    url(r'login/',views.loginuser,name="login"),

    


]
