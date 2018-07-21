from rest_framework.views import APIView
from rest_framework.response import Response
from daily_tracker.models import Attandance
from .serializers import AttandanceSerializer


class AttandanceList(APIView):
    def get(self, request):
        attandances = Attandance.objects.all()
        serializer = AttandanceSerializer(attandances, many=True)
        return Response(serializer.data)
