from django.conf.urls import url
from django.urls import path
from .import views



urlpatterns = [
   url(r'^$',views.articles_list,name ="list"),
   url(r'^(?P<slug>[\w-]+)/$',views.articles_details,name="detail"),
 #  path('<slug>/',views.articles_details, name='details'),

]