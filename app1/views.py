from django.shortcuts import render


def jinja(request):
    d={'name':'Honey Rose'}
    return render(request,'Adhi.html',d)