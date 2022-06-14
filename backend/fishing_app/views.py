from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
