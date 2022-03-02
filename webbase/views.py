from django.shortcuts import render

from .models import AlbiDOro
 
def homeViews(request): 
    context = {}
    return render(request, "index.html", context )

def albiDoroViews(request): 
    albiDoro = AlbiDOro.objects.all()
    context = {'albiDoro':albiDoro}
    return render(request, "albidoro.html", context )

 