from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items', views.items, name='items'),
    url(r'^students', views.students, name='students'),
    url(r'^users', views.users, name='users'),
    url(r'^history', views.checkoutHistory, name='checkoutHistory'),
    url(r'^checkin/(?P<checkout_id>[0-9]+)/$', views.checkin, name='checkin'),
    
]
#