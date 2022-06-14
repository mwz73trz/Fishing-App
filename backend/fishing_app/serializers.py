from rest_framework.serializers import ModelSerializer
from .models import *

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'date', 'place', 'water', 'temperature', 'sky', 'wind', 'water', 'type_fishing', 'note']
