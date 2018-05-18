from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.LeaveCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.LeaveUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LeaveDeleteView.as_view(), name='delete'),
    path('', views.LeaveListView.as_view(), name='leave_list'),
    path('<int:pk>', views.LeaveDetailView.as_view(), name='detail'),
]
