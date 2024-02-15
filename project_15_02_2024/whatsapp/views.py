from rest_framework import viewsets 
from .serializers import WhatsappSerializer
from .models import Whatsapp


class WhatsappViewSet(viewsets.ModelViewSet):
    serializer_class = WhatsappSerializer
    queryset = Whatsapp.objects.all()