from django.contrib import admin

from .models import Item, User, Checkout

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Checkout)

# Register your models here.
