from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import os
# Create your views here.


@login_required
def send(request):
    if request.method == 'POST':
        send_mail('Hello from perficient.com',
                  'hi hello this is automated message.',
                  os.environ.get('GM_USER'),
                  ['perficient@emailna.co'],
                  fail_silently=False
                  )
    return render(request, 'send/mail.html')
