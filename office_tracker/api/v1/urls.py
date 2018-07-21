from django.urls import path, include

urlpatterns = [
    path('v1/', include(('api.v1.daily_tracker.urls', 'daily_tracker'), namespace='daily_tracker')),
]
