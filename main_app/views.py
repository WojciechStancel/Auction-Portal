from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,
                  'main_app/home.html')


def about_us(request):
    return render(request, 'main_app/about_us.html')
