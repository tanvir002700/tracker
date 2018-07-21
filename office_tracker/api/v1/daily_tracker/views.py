from rest_framework import generics
from daily_tracker.models import Attandance
from .serializers import AttandanceSerializer
from rest_framework import viewsets
from rest_framework import permissions


class AttandanceList(viewsets.ReadOnlyModelViewSet):
    queryset = Attandance.objects.all()
    serializer_class = AttandanceSerializer
    permission_classes = (permissions.IsAuthenticated,)
