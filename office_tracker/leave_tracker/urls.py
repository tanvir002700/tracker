from django.conf.urls import url
from . import views

urlpatterns = [
    url('^create/$', views.LeaveCreateView.as_view(), name='create'),
    url('^leave_list/$', views.LeaveListView.as_view(), name='leave_list')
]
