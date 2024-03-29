from django.shortcuts import render

# Create your views here.
from django.views import generic

from Loginapp.forms import login_frm
from adminapp.models import User,Trainer,Hr

def login(request):
    if request.method=='GET':
        form=login_frm()

    if request.method=='POST':
         form=login_frm(request.POST)

         if form.is_valid():
             print("form is valid")
             role = request.POST.get('role')
             print(role)
             username=form.cleaned_data['username']
             pwd = form.cleaned_data['password']
             print(username)

             if role == "HR":
                 print ("role HR verified")
                 if Hr.objects.filter(hr_username=username).filter(hr_password=pwd):
                     print("login successfull")
                     #data = Hr.objects.get(hr_username=username)
                     return render(request, 'adminapp/hrbase.html', {'form':form})
                 else:
                        print("invalid username or password")


             elif role == "Student":
                 print ("Student verified")
                 # if User.objects.filter(user_username=username).filter(user_password=pwd):
                 #     print("login successfull")
                 # else:
                 #        print("invalid username or password")


             elif role == "Trainer":
                 print("Trainer verified")
                 # if Trainer.objects.filter(trainer_username=username).filter(trainer_password=pwd):
                 #     print("login successfull")
                 # else:
                 #        print("invalid username or password")







    return render(request, 'Loginapp/login_page.html', {'form': form})