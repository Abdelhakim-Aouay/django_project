from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add, name='add'),
    path('show/',views.show, name='show'),
    path('supp/<int:id>',views.supp, name='supp'),
    path('modifier/<int:id>',views.modifier, name='modifier'),
    path('update/<int:id>',views.update, name='update'),
    
    
]