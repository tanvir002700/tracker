from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .daily_tracker.views import AttandanceList

router = routers.DefaultRouter()
router.register(r'daily_trackers', AttandanceList)

urlpatterns = [
    path(r'', include(router.urls))
]
