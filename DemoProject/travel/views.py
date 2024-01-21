from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dests = Destination.objects.all()
    
    
    
    # des1 = Destination()
    # des1.name = "Munich"
    # des1.desc = "City of Bayern Munich"
    # des1.price = 800
    # des1.img = 'destination_1.jpg'
    # des1.offers = False
    
    # des2 = Destination()
    # des2.name = "Berlin"
    # des2.desc = "Capital of Germany"
    # des2.price = 850
    # des2.img = 'destination_2.jpg'
    # des2.offers = True
    
    # des3 = Destination()
    # des3.name = "Hamburg"
    # des3.desc = "One of the Beautiful city"
    # des3.price = 790
    # des3.img = 'destination_3.jpg'
    # des3.offers = True
    
    # dests = [des1, des2, des3]
    
    return render(request, "index.html", {'dests': dests})