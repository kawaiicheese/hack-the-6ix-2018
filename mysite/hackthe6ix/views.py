from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Person

# Create your views here.
def index(request):	
	return render(request, 'hackthe6ix/profile.html')
	try:
		if Person.objects.get(email=request.POST['username'],password=request.POST['pass']) :
			i = 0
			# for now, dont care about if correct photo matches correct person. just populate it
			imgurLink = []
			for person in Person.objects.all():
				i += 1
				imgurLink.append(person.profilepic)
			return render(request, 'hackthe6ix/index.html', {'arrLength':i, 'imgurLink':imgurLink})
	except Exception as e:
		print(e)
	return render(request, 'hackthe6ix/login.html')

def registration(request):
	return render(request, 'hackthe6ix/registration.html')

def verify(request):
	email = request.POST['email']
	password = request.POST['password']

	try:
		if Person.objects.get(email = email):
			return render(request, 'hackthe6ix/registration.html')
	except Exception:
		pass
	person = Person(email = email, password = password, 
					first_name = request.POST['first_name'], last_name = request.POST['last_name'],
				    age = request.POST['age'], gender = True, profilepic = request.POST['profilepic'])
	person.save()
	return render(request, 'hackthe6ix/verify.html')

def map(request):
	return render(request, 'hackthe6ix/map.html')