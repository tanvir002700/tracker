from rest_framework import generics
from daily_tracker.models import Attandance
from .serializers import AttandanceSerializer


class AttandanceList(generics.ListAPIView):
    queryset = Attandance.objects.all()
    serializer_class = AttandanceSerializer
