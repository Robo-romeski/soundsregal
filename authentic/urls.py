from django.conf.urls import url
from authentic import views
from django.contrib.auth import login
from django.contrib.auth import views
from authentic.views import indexView

urlpatterns = [
#url(r'^registration/', views.signout, name='signout'),
url(r'^login/$', views.login, name='login'),
#url(r'^sign/$', views.home, name='home'),
url(r'^$', indexView.as_view()),
]
