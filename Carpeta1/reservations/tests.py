from django.test import TestCase
from django.utils import timezone
from reservations.models import Reservation
from reservations.serializers import reservationSerializer

class ReservationAPITest(TestCase):
    def test_future_date_validation(self):
        future_date = timezone.now().date() + timezone.timedelta(days=3)
        serializer = reservationSerializer(data={'name': 'Test', 'date': future_date, 'numberGuests': 5})
        self.assertTrue(serializer.is_valid())

    def test_past_date_validation(self):
        past_date = timezone.now().date() - timezone.timedelta(days=1)
        serializer = reservationSerializer(data={'name': 'Test', 'date': past_date, 'numberGuests': 5})
        self.assertFalse(serializer.is_valid())
        self.assertIn('La fecha no puede estar en el pasado', serializer.errors['date'])

    def test_guests_validation(self):
        serializer = reservationSerializer(data={'name': 'Test', 'date': timezone.now().date(), 'numberGuests': 0})
        self.assertFalse(serializer.is_valid())
        self.assertIn('El número de huéspedes debe ser mayor a 0', serializer.errors['numberGuests'])


