from django.urls import path, include

urlpatterns = [
    path('daily_tracker/', include(('api.v1.daily_tracker.urls', 'daily_tracker'), namespace='daily_tracker')),
]
