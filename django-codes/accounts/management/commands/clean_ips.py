from typing import Any, Optional
from django.core.management.base import BaseCommand
from core.models import BlockedIps

class Command(BaseCommand):
    help = "All blocked ips cleaned"

    def handle(self, *args: Any, **options: Any):
        x = BlockedIps.objects.all()
        x.delete()
