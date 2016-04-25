from django.forms import *

from .models import User


class OtherCheckoutForm(forms.Form):
    user_id = ModelChoiceField(queryset=User.objects.all().order_by('first_name'))


class CheckoutForm(ModelForm):
    item_id = CharField()

    class Meta:
        model = User
        fields = ['student_id', 'first_name', 'last_name', 'email']
