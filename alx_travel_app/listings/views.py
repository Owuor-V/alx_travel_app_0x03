from rest_framework.response import Response
from rest_framework import status
from .tasks import send_booking_confirmation_email


def perform_create(self, serializer):
    booking = serializer.save()
    user_email = booking.user.email
    destination = booking.destination.name
    booking_id = booking.id

    # Trigger Celery Email Task
    send_booking_confirmation_email.delay(user_email, destination, booking_id)
