from django.shortcuts import render
from django.utils import timezone
from .models import Item

from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'checkout/index.html', {})
    

def items(request):
    items = Item.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'checkout/listitems.html', {'items': items})
#def getItems(request):
    
def users(request):
    return HttpResponse("<html><b>This will be the users page")

def students(request):
    return HttpResponse("<html><b>This will be the students page")

def checkoutHistory(request):
    return HttpResponse("<html><b>This will be the checkout history page</b></html>")