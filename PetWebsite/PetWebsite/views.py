from django.shortcuts import render_to_response
from pets.models import Pet,Contact
from django.template import RequestContext

	



def adopt(request):

	
	contacts = Contact.objects.all()
	pets = Pet.objects.all()

	if  request.POST:
		
		pet_name=request.POST['data']
		pet = Pet.objects.get(name=pet_name)
		
		return render_to_response('petdata.html',locals())
	else:
		return render_to_response('adopt.html',locals())

	return render_to_response('adopt.html',locals())
	
def sssl(request):
	return render_to_response('homepage.html',locals())

def homepage(request):
	return render_to_response('homepage.html',locals())

def adopted(request):
	if request.POST:
		pet_name=request.POST['pet_name']
		pet_age=request.POST['pet_age']
		pet_gender=request.POST['pet_gender']
		sterilization=request.POST['sterilization']
		health=request.POST['health']
		other=request.POST['other']

		contact=request.POST['contact']
		contact_gender=request.POST['contact_gender']
		phone=request.POST['phone']
		email=request.POST['email']
		address=request.POST['address']

		
		Contact.objects.create(
			name=contact,
			gender=contact_gender,
			phone=phone,
			email=email,
			address=address,
			#pet_name=Pet.objects.get(name=pet_name)

			)
		Pet.objects.create(
			name=pet_name,
			age=pet_age,
			gender=pet_gender,
			sterilization=sterilization,
			other=other,
			health=health,
			contact=Contact.objects.get(name=contact),
			)
	return render_to_response('adopted.html',RequestContext(request,locals()))

def found(request):
	return render_to_response('found.html',locals())

def notice(request):
	return render_to_response('notice.html',locals())

def lost(request):
	return render_to_response('lost.html',locals())

def process(request):
	return render_to_response('process.html',locals())

def signup(request):
	return render_to_response('signup.html',locals())

def login(request):
	return render_to_response('login.html',locals())

def takemehome(request):
	return render_to_response('takemehome.html',locals())

def bringmedetail(request):
	return render_to_response('bringmedetail.html',locals())

def team(request):
	return render_to_response('team.html',locals())

def contact(request):
	return render_to_response('contact.html',locals())

def bringmedetail(request):
	return render_to_response('bringmedetail.html',locals())




