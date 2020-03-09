from django.conf.urls import url, include
from apps.gestion.views import Login

urlpatterns = [
  #  url(r'^$', index),
   url(r'^$', Login.as_view(), name="login"),
]


