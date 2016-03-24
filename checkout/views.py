from django.shortcuts import render
from django.utils import timezone
from .models import Item, User, Checkout

from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'checkout/index.html', {})
    

def items(request):
    checkouts = Checkout.objects.all().order_by('item__category'.capitalize)
    return render(request, 'checkout/listitems.html', {'checkouts': checkouts})
#def getItems(request):
    
def users(request):
    return HttpResponse("<html><b>This will be the users page")

def students(request):
    return HttpResponse("<html><b>This will be the students page")

def checkoutHistory(request):
    return HttpResponse("<html><b>This will be the checkout history page</b></html>")