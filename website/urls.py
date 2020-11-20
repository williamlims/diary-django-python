from django.urls import path

from . import views

urlpatterns = [

    path('login/', admin.site.urls, name='login'),
    
]
