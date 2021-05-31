from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def homepage(request):
    return render(request,"Home.html")

def contacts(request):
    return render(request,"Contact.html")

def SubmitContact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message,date=datetime.today())
        
        contact.save()
        messages.success(request,"Your response has been successfully submitted!")
        return render(request,"Contact.html")
        