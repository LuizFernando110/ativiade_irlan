from django.shortcuts import render

def dashBoard(request):
    return render(request,"enquetes-index.html")