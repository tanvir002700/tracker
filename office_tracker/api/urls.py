from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .daily_tracker.views import AttandanceList


urlpatterns = [
    path('api_test', AttandanceList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
