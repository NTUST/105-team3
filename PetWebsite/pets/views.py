from django.shortcuts import render_to_response
from pets.models import Pet,Contact
from django.template import RequestContext

	
def adopt(request):
	pets = Pet.objects.all()
	
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

		contact_name=request.POST['contact_name']
		contact_gender=request.POST['contact_gender']
		phone=request.POST['phone']
		email=request.POST['email']
		address=request.POST['address']

		Pet.objects.create(
			name=pet_name,
			age=pet_age,
			gender=pet_gender,
			sterilization=sterilization,
			other=other,
			health=health
			#contact_name=Contact.objects.get(name=contact_name)
			)
		Contact.objects.create(
			name=contact_name,
			gender=contact_gender,
			phone=phone,
			email=email,
			address=address,
			pet_name=Pet.objects.get(name=pet_name)

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