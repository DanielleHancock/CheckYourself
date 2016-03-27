from django.shortcuts import render
from django.utils import timezone
from .models import Item, User, Checkout

from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'checkout/index.html', {})
    

def items(request):
    checkouts = {checkout.item.item_id: checkout for checkout in Checkout.objects.filter(checkin_date__isnull=True)}
    
    items = []
    for item in Item.objects.all().order_by('category'):
        checkout = checkouts.get(item.item_id)
        items.append((item,checkout))
    print("x" for item in items)
                 
    """items = Item.objects.all().select_related('checkout').filter(checkout__checkin_date__isnull=False) #Checkout.objects.all().order_by('item__category')"""
    
    return render(request, 'checkout/listitems.html', {'items': items})


def users(request):
    return HttpResponse("<html><b>This will be the users page")

def students(request):
    return HttpResponse("<html><b>This will be the students page")

def checkoutHistory(request):
    return HttpResponse("<html><b>This will be the checkout history page</b></html>")