from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import AttandanceList

router = routers.DefaultRouter()
router.register(r'attandances', AttandanceList)

urlpatterns = [
    url(r'', include(router.urls))
]
