from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from faker import Faker
fake = Faker()
from django.contrib.auth import get_user_model
User = get_user_model()

class Command(BaseCommand):
    help = "Used to create users"
    requires_migrations_checks = True

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--number', type=int, default=10)

    def handle(self, *args: Any, **options: Any):
        for i in range(1, options['number'] + 1):
            print(f'{i} user created')
            User.objects.create_user(
                username = fake.name(),
                email = fake.email()
            )
