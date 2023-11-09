from django.shortcuts import render

# Create your views here.
def ammu(request):
    return render(request,'ammu.html')

def nani(request):
    return render(request,'nani.html')

def mokshi(request):
    return render(request,'mokshi.html')

def hari(request):
    return render(request,'hari.html')