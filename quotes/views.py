from django.shortcuts import render, redirect
from django.contrib import messages
from  .models import QuoteRequest

def services_page(request):
    return render(request,'services.html')

def home_page(request):
    return render(request,'home.html')

def about_page(request):
    return render(request,'about.html')

def submit_quote(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # save to database
        QuoteRequest.objects.create(name=name,email=email,message=message)

        messages.success(request,"your quote has been sent successfully!")

        return redirect("services")

        return render(request,'services.html')

