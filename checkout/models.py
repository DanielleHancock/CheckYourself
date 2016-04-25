from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    student_id = models.CharField(max_length=8,primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    def __str__(self):
        return self.first_name+" "+self.last_name+": "+str(self.student_id)
    
    #leaving out password for now
    #to add new Item:
    #i = Item(checked_out=False,serial_number="39452",model_number="Raspberry Pi 2",purchase_date=timezone.now(),category="Raspberry Pi",description="Really cool pi")
    
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    kit_number = models.IntegerField(blank=True, null=True)
    checked_out = models.BooleanField(default=False)
    serial_number = models.CharField(max_length=20) # check whether this is right
    model_number = models.CharField(max_length=50, blank=True, null=True)
    purchase_date = models.DateField('date purchased')
    category = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
                        
    def __str__(self):
        return self.category

class Checkout(models.Model): #by not specifying a primary key, django will create an autoincrementing field to be the primary key
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User,related_name='borrower',null=True,on_delete=models.SET_NULL)
    authorizer = models.ForeignKey(User,related_name='authorizer',null=True,on_delete=models.SET_NULL)
    checkout_date = models.DateField('checkout date')
    checkin_date = models.DateField('checkin date',null=True,blank=True)
    
    def __str__(self):
        return str(self.checkout_date)
        
