from django.conf.urls import url
from . import views

urlpatterns = [
    url('^create/$', views.LeaveCreateView.as_view(), name='create')
]
