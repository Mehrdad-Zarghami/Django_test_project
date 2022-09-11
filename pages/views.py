from django.shortcuts import render
from django.http import HttpResponse

""" a ready-to-use response class that shows
 a webpage with its input text('Hello Mehrdad') 
"""
#  Create your views here.
def e_shop(request):
    context = {
        'greeting':'سلام و درود بر شما',
        'country':'Iran',
        'button_value': 'Click Me Bitch',
    }
    return render(request, 'home.html', context=context)


def about(request):
    return render(request, 'pages/about.html')


def contact_us(request):
    context={
        'phone_number': '00989179991922',
        'gmail': 'mehrdad.zarghami69@gmail.com',
    }
    return render(request, 'pages/contact_us.html', context=context)
