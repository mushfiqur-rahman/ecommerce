from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message', 'from@moshbuy.com', ['john@moshbuy.com'])
        message.attach_file('playground/static/images/park.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'index.html', {'name': 'Mushfiq'})
