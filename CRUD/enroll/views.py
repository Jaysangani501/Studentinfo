from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import Studentregistration
from .models import user
# Create your views here.

def add_show(request):
    if request.method == 'POST':
         fm = Studentregistration(request.POST)
         if fm.is_valid():
              nm = fm.cleaned_data['name']
              em = fm.cleaned_data['email']
              pw = fm.cleaned_data['password']
              reg = user(name=nm,email=em,password=pw)
              reg.save()
              fm = Studentregistration()
    else:
     fm = Studentregistration()
    stud = user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


def delete_data(request,id):
    if request.method == 'POST':
     pi = user.objects.get(pk=id)
     pi.delete()
     return HttpResponsePermanentRedirect('/')


def update_data(request,id):
   if request.method == 'POST':
     pi = user.objects.get(pk=id)
     fm = Studentregistration(request.POST,instance=pi)
     if fm.is_valid():
        fm.save()
   else:
      pi = user.objects.get(pk=id)
      fm = Studentregistration(instance=pi)
      
   return render(request,'enroll/updatestudent.html',{'form':fm})