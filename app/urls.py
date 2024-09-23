from django.urls import path
from . import views
urlpatterns=[
    path('about/',views.about,name='about'),
    path('careers/',views.careers,name='careers'),
    path('contact/',views.contact,name='contact'),
    path('prjct/',views.prjct,name='prjct'),
    path('services/',views.services,name='services'),

]