from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create hardcoded users'

    def handle(self, *args, **kwargs):
        users = [
            {'username': 'user1', 'password': 'password1'},
            {'username': 'user2', 'password': 'password2'},
        ]

        for user_data in users:
            user, created = User.objects.get_or_create(username=user_data['username'])
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully created user {user_data["username"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user_data["username"]} already exists'))
