from django.shortcuts import render, redirect
import smtplib


def home(request):
    return render(request,'home.html')

def send_mail(request):
    content = 'example email content'

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('khalifngeno@gmail.com','Poheri333')

    mail.sendmail('khalifngeno@gmail.com','sethkrm@gmail.com',content)

    mail.close()

    print('Email Sent')
    
    return redirect(home)

