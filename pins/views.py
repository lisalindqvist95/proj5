from rest_framework import generics, permissions
from proj5.permissions import IsOwnerOrReadOnly
from pins.models import Pin
from pins.serializers import PinSerializer

# CREDIT: Adapted from the Code Institute DRF Tutorial Project
# URL:    https://github.com/Code-Institute-Solutions/drf-api


class PinList(generics.ListCreateAPIView):
    """
    List pins or create a pin if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PinSerializer
    queryset = Pin.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PinDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a pin or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PinSerializer
    queryset = Pin.objects.all()
