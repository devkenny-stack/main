from django.shortcuts import render, redirect
from .models import Admission, ContactMessage
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def admissions(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        grade = request.POST['grade']
        message = request.POST['message']
        
        Admission.objects.create(full_name=full_name, email=email, phone=phone, grade=grade, message=message)
        messages.success(request, 'Your application has been submitted!')
        return redirect('admissions')

    return render(request, 'admissions.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent!')
        return redirect('contact')

    return render(request, 'contact.html')
