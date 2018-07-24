"""office_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from daily_tracker.views import AttandanceListView

urlpatterns = [
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('daily_tracker/attandances/', include(('daily_tracker.urls', 'daily_tracker'), namespace='daily_tracker')),
    path('leave_tracker/', include(('leave_tracker.urls', 'leave_tracker'), namespace='leave_tracker')),
    path('api/api-auth', include('rest_framework.urls')),
    path('api/v1/', include(('api.v1.urls', 'api'), namespace='api')),
    path('admin/', admin.site.urls),
    path('', AttandanceListView.as_view(), name='root')
]
