from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Person, Listings
from .listing import getList

userUID = 0
loggedIn = False

# Create your views here.
def index(request):
	try:
		global userUID
		global loggedIn
		# when user logs in with correct password
		person = Person.objects.get(email=request.POST['username'],password=request.POST['pass'])
		if person :
			userUID = person.id
			loggedIn = True
			return render(request, 'hackthe6ix/index.html', {'data':getList()})
	except Exception as e:
		try:
			# when seller submits a form.
			user = Person.objects.get(pk=userUID)
			listForm = Listings.objects.create(person=user, address = request.POST['address'], gender = request.POST['gender'],
								price = request.POST['price'], phone = request.POST['phone'],
								propertypic = request.POST['propertypic'], lease = request.POST['lease'], description=request.POST['description'])
			listForm.save()

			return render(request, 'hackthe6ix/index.html', {'data':getList()})
		except Exception as e:
			print(e)
	if loggedIn:
		return render(request, 'hackthe6ix/index.html', {'data':getList()})

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
				    age = request.POST['age'], gender = request.POST['gender'], profilepic = request.POST['profilepic'])
	person.save()
	return render(request, 'hackthe6ix/verify.html')

def map(request):
	return render(request, 'hackthe6ix/map.html')

def profile(request):
	return render(request, 'hackthe6ix/profile.html')

def listform(request):
	return render(request, 'hackthe6ix/listform.html')