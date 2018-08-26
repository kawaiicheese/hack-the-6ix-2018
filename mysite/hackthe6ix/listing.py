from .models import Person, Listings

def getList():
	toRet = []
	listings = Listings.objects.all()
	for listing in listings:
		toPut = {}
		toPut['address'] = listing.address
		toPut['price'] = listing.price
		toPut['gender'] = listing.gender
		toPut['lease'] = listing.lease
		toPut['phone'] = listing.phone
		toPut['propertypic'] = listing.propertypic
		toPut['email'] = listing.person.email
		toPut['first_name'] = listing.person.first_name
		toPut['last_name'] = listing.person.last_name
		toPut['age'] = listing.person.age
		toPut['profilepic'] = listing.person.profilepic		
		toPut['description']=listing.description
		toRet.append(toPut)
	return toRet