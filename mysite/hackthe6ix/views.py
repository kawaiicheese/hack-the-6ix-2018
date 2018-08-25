from django.shortcuts import render

# Create your views here.
def index(request):	
	return render(request, 'hackthe6ix/login.html')

def registration(request):
	return render(request, 'hackthe6ix/registration.html')

def verify(request):
	return render(request, 'hackthe6ix/verify.html')
