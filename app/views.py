from django.shortcuts import render,redirect
from django.views.generic import View
from django.db.models import Q
from .forms import *
from .models import *

# Create your views here.

class Signup(View):
    def get(self,request):
        form = UserForm()
        return render(request,'signup.html',{"form":form})

    def post(self,request):
        form  = UserForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('login')


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            username = self.request.POST.get('email')
            password = self.request.POST.get('password')

        cond = Q(email = username) & Q(password = password)

        check =User.objects.filter(cond).count()

        if (check == 1):
            request.session['login'] = username
            return redirect('cal')
        else:
            return redirect('login')

# def sum(x,n):
#     total = 0
#     for i in range(1,n+1):
#         total+=1/(x**i)
#         return total
#
# print(sum(1,3))


def Sum(x,n):
    if n==1:
        return 1/x
    a = Sum(x,n-1)+1/(x**n)
    return a

class Calculation(View):
    def get(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')
        return render(request,'getdata.html')

    def post(self,request,*args,**kwargs):
        if not request.session.has_key('login'):
            return redirect('login')

        x = request.POST.get('x')
        n = request.POST.get('n')

        x = int(x)
        n = int(n)
        a = Sum(x,n)
        data = {"result":a}
        return render(request,'result.html',data)








