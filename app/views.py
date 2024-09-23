import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

# def careers(request):
#     if request.method=="POST":
#         name=request.POST.get("Name")
#         phone=request.POST.get("phone")
#         email=request.POST.get("email")
#         role=request.POST.get("role")
#
#         subject=f"Application for {role}"
#         message=f"Hi {name},\nThank you for applying for the position {role}"
#         email_from=settings.EMAIL_HOST_USER
#         recipient_list=[email]
#         send_mail(subject,message,email_from,recipient_list)
#
#     return render(request,"careers.html")

def careers(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        role = request.POST.get("role")

        subject = f"Application for {role}"
        message = f"Hi {name},\nThank you for applying for the position {role}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]

        try:
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Your application has been submitted successfully!')
        except Exception as e:
            messages.error(request, 'Error sending email. Please try again.')

    return render(request, "careers.html")

def contact(request):
    return render(request,'contact.html')

def prjct(request):
    return render(request,'prjct.html')

def services(request):
    return render(request,'services.html')








