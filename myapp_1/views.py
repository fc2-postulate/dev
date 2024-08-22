from django.shortcuts import render

def home(request):
    return render(request, 'myapp_1/index.html')