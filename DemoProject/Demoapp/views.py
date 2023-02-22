# from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,"home.html")
#
# def about(request):
#     return HttpResponse("ALL ABOUT ME")
#
# def contact(request):
#     return render(request,"contact.html")
#
# def details(request):
#     return HttpResponse("FULL DETAILS HERE")
#
# def thanks(request):
#     return render(request,"thanks.html")


#additional question
#
# def home(request):
#      return render(request,"home.html")

# def result(request):
#     x=int(request.POST["num1"])
#     y=int(request.POST['num2'])
#     add=(x+y)
#     sub=(x-y)
#     div=(x//y)
#     multi=(x*y)
#     return render(request,"results.html",{"addition":add,"subtract":sub,"division":div,"multiplication":multi})

# static webpage

from django.shortcuts import render
from .models import Place
from .models import People

def demo(request):
    obj=Place.objects.all()
    orj=People.objects.all()
    return render(request,"index.html",{'result':obj,'replace':orj})