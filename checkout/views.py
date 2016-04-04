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
        items.append((item, checkout))

    return render(request, 'checkout/listItems.html', {'items': items})


def students(request):
    student_list = [student for student in User.objects.filter(user_type="STUDENT")]
    print(student for student in student_list)
    return render(request, 'checkout/listStudents.html', {'students': student_list})


def users(request):
    return HttpResponse("<html><b>This will be the users page")


def checkoutHistory(request):
    checkouts = {checkout.item.item_id: checkout for checkout in Checkout.objects.all()}

    items = []
    for item in Item.objects.all().order_by('category'):
        checkout = checkouts.get(item.item_id)
        items.append((item, checkout))

    return render(request, 'checkout/checkoutHistory.html', {'items': items})
