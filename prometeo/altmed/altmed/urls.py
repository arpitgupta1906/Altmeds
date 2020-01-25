from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^core/',include('core.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
