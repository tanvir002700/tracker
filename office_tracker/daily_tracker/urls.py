from django.urls import path
from . import views

urlpatterns = [
    path('login', views.DailyLoginView.as_view(), name='login'),
    path('logout', views.DailyLogoutView.as_view(), name='logout'),
    path('', views.AttandanceListView.as_view(), name='attandance_list'),
    path('today', views.TodayAttandanceListView.as_view(), name='today_attandance_list')
]
