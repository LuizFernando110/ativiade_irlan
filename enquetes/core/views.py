from django.shortcuts import render

# Create your views here.

def paginaIncial(request):
    return render(request,'core-index.html')