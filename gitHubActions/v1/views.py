from rest_framework import generics
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status

class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class StaticListAPIView(APIView):
    def get(self, request):
        data = [
            {"id": 1, "name": "Arul", "role": "Developer"},
            {"id": 2, "name": "Vijay", "role": "Tester"},
            {"id": 3, "name": "Kumar", "role": "Manager"},
        ]
        return Response(data, status=status.HTTP_200_OK)