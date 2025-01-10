from rest_framework import generics
from backend_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    # List all profiles; creation is handled by django signals
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateAPIView):
    # Fetch, update & delete profile if User == Owner
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer