from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Person, User

# Create your views here.
def index(request):	
	try:
		if User.objects.get(email=request.POST['username'],password=request.POST['pass']) :
			return render(request, 'hackthe6ix/index.html')
	except Exception:
		print("exception")
	return render(request, 'hackthe6ix/login.html')

def registration(request):
	return render(request, 'hackthe6ix/registration.html')

def verify(request):
	email = request.POST['email']
	password = request.POST['password']

	try:
		if User.objects.get(email = email):
			return render(request, 'hackthe6ix/registration.html')
	except Exception:
		pass
	user = User(email = email, password = password)
	person = Person(first_name = request.POST['first_name'], last_name = request.POST['last_name'],
				    age = request.POST['age'], gender = True)
	user.save()
	person.save()
	return render(request, 'hackthe6ix/verify.html')

def map(request):
	return render(request, 'hackthe6ix/map.html')