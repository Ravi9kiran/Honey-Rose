from django.shortcuts import render

def Ravi(request):
    R={'name':'chandrika Ravi'}
    return render(request,'pavan.html',R)
