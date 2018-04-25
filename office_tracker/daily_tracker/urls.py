from django.conf.urls import url
from . import views

urlpatterns = [
    url('^login/$', views.DailyLoginView.as_view(), name='login'),
    url('^logout/$', views.DailyLogoutView.as_view(), name='logout')
]
