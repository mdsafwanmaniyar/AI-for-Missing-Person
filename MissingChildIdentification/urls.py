from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from missingchild.views import login,addmissingchild,viewmissingperson,deletemissingperson,logout,findMissingPerson,viewrecordedpersons,viewuserprofile,userregistration

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='login'),
    path('login/', TemplateView.as_view(template_name='index.html'), name='login'),
    path('loginaction/',login, name='loginaction'),

    path('userregistration/', TemplateView.as_view(template_name='registration.html'), name='registration'),
    path('userregaction/', userregistration, name='regaction'),

    path('addmissingchild/', TemplateView.as_view(template_name='addmissingperson.html'), name='registration'),
    path('addmissingchildaction/',addmissingchild, name='regaction'),

    path('viewmissingperson/',viewmissingperson,name='transactions'),
    path('deletemissingperson/',deletemissingperson,name='transactions'),

    path('findMissingPerson/',findMissingPerson,name='transactions'),
    path('viewrecordedpersons/',viewrecordedpersons,name='transactions'),
    path('viewuserprofile/',viewuserprofile,name='transactions'),

    path('logout/',logout,name='logout'),
]
