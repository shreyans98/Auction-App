from django.shortcuts import render

from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import vendorProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer

# Create your views here.

def index(request):
    return render(request, 'auction/index.html')


class vendorProfileListCreateView(ListCreateAPIView):
    queryset=vendorProfile.objects.all()
    serializer_class=vendorProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class vendorProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=vendorProfile.objects.all()
    serializer_class=vendorProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]
    
    


