from django.shortcuts import render


def index(request):
    conext ={

    }
    return render(request,'todo/index.html',conext)