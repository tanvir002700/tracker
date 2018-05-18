from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.LeaveCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.LeaveUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.LeaveDeleteView.as_view(), name='delete'),
    path('leave_list/', views.LeaveListView.as_view(), name='leave_list'),
]
