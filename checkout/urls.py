from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items', views.items, name='items'),
    url(r'^students', views.students, name='students'),
    url(r'^users', views.users, name='users'),
    url(r'^history', views.checkoutHistory, name='checkoutHistory'),
    url(r'^checkin/(?P<checkout_id>[0-9]+)/$', views.checkin, name='checkin'),
    url(r'^search_items', views.search_items, name='search_items'),
    url(r'^search_students', views.search_students, name='search_students'),
    
]
#