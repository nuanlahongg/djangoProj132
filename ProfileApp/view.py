from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<H1> Hello Word <br> This is my Word wide web </H1>")

def home(request):
    return render(request, 'home.html')

def personalRecord(request):
    return render(request, 'personalRecord.html')

def educationalRecord(request):
    return render(request, 'educationalRecord.html')

def interests(request):
    return render(request, 'interests.html')

def product(request):
    return render(request, 'product.html')

def roleModel(request):
    return render(request, 'roleModel.html')


