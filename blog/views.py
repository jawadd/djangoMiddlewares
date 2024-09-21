from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    print("Home Page View")
    return HttpResponse("This is home page view")
