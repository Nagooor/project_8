from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':5010,'b':5002,'c':5001}
    return render(request,'conditions.html',d)