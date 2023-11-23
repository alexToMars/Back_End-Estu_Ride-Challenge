from rest_framework import serializers
from .models import Reservation
from django.utils import timezone

class reservationSerializer(serializers.ModelSerializer):

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError('La fecha no puede estar en el pasado')
        return value

    def validate_numberGuests(self, value):
        if value <= 0:
            raise serializers.ValidationError('El número de huéspedes debe ser mayor a 0')
        return value
    class Meta:
        model = Reservation
        fields = '__all__'
