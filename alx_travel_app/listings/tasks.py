from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation_email(email, destination, booking_id):
    subject = "Booking Confirmation"
    message = f"Your booking for {destination} has been confirmed! Booking ID: {booking_id}."
    from_email = "no-reply@travelapp.com"

    send_mail(subject, message, from_email, [email])
    return "Email sent successfully"
