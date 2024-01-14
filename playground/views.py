from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render
from store.models import Product


def say_hello(request):
    try:
        send_mail('subject', 'message', 'john@moshbuy.com', ['dragoonsbd@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'index.html', {'name': 'Mushfiq'})
