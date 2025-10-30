# alx_travel_app/listings/management/commands/seed.py
from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Cozy Beach House",
                "description": "A beautiful house by the sea.",
                "price_per_night": 120.00,
                "location": "Mombasa",
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "price_per_night": 75.00,
                "location": "Nairobi",
            },
            {
                "title": "Safari Lodge",
                "description": "Enjoy nature in this unique lodge.",
                "price_per_night": 150.00,
                "location": "Maasai Mara",
            },
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
