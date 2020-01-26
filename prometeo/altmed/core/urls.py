from django.conf.urls import url
from core import views# SET THE NAMESPACE!
app_name = 'core'# Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^headache/$',views.headache1,name='headache'),
    url(r'^malaria/$',views.malaria1,name='malaria'),
]
