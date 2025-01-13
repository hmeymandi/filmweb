from django.shortcuts import render,HttpResponse

# Create your views here.

def testpages(request):
    return HttpResponse ("Test page")