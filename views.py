from django.shortcuts import render,redirect
# from .forms import productform
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def products(request):
    return render(request,'products.html')
def login(request):
    return render(request,'login.html')
def registration(request):

    #     myform=productform(request.POST)
    #     if myform.is_valid():
    # if request.method=='POST':
    #         myform.save()
    #         return redirect('login')
    #     return redirect('registration')
    # pyhon manage.py
    # else:
    #     myform=productform()
    return render(request,'registration.html')
def contact(request):
    return render(request,'contact.html')





# Create your views here.
