from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from daily_tracker.models import Attandance
from .serializers import AttandanceSerializer


class AttandanceList(viewsets.ReadOnlyModelViewSet):
    queryset = Attandance.objects.all()
    serializer_class = AttandanceSerializer
    permission_classes = (IsAuthenticated,)
