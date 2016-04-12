from django.shortcuts import render
from django.utils import timezone
from .models import Item, User, Checkout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'checkout/index.html', {})

@login_required
def items(request):
    checkouts = {checkout.item.item_id: checkout for checkout in Checkout.objects.filter(checkin_date__isnull=True)}

    items = []
    for item in Item.objects.all().order_by('category'):
        checkout = checkouts.get(item.item_id)
        items.append((item, checkout))

    return render(request, 'checkout/listItems.html', {'items': items})


def checkin(request, checkout_id):
    checkout_object = Checkout.objects.get(pk=checkout_id)
    checkout_object.checkin_date = timezone.now()
    checkout_object.item.checked_out = False
    checkout_object.save()
    print("checkin")
    return HttpResponse(status=204)


def students(request):
    student_list = [student for student in User.objects.filter(user_type="STUDENT")]
    print(student for student in student_list)
    return render(request, 'checkout/listStudents.html', {'students': student_list})


def users(request):
    return HttpResponse("<html><b>This will be the users page")


def checkoutHistory(request):
  
    
    checkouts = Checkout.objects.all()
   
    
    return render(request, 'checkout/checkoutHistory.html',{'checkouts': checkouts})
