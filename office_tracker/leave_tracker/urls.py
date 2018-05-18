from django.urls import path
from . import views

urlpatterns = [
    path('create', views.LeaveCreateView.as_view(), name='create'),
    path('leave_list', views.LeaveListView.as_view(), name='leave_list'),
    path('update/<int:pk>', views.LeaveUpdateView.as_view(), name='update')
]
