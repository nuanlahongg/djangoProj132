from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<H1> Hello Word <br> This is my Word wide web </H1>")

def home(request):
    return render(request, 'homePage.html')

def personalRecord(request):
    return render(request, 'secondPage.html')

def educationalRecord(request):
    return render(request, 'thirdPage.html')

def interests(request):
    return render(request, 'fourthPage.html')

def product(request):
    return render(request, 'fivePage.html')

def roleModel(request):
    return render(request, 'sixthPage.html')


