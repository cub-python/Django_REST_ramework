from django.core.management.base import BaseCommand
from users_app.models import User

class Command(BaseCommand):
    help = 'Create Superuser and some test users'

    def add_arguments(self, parser):
        parser.add_argument('count, type=int')

    def handle(self, *args, **options):
        User.objects.all().delete()
        user_count = options['count']
        User.objects.create_superuser('Nikola','Nikola@test.ru', 'usertest1')
        for i in range(user_count):
            User.objects.create_user(f'user{i}', f'user{i}@test.ru', 'usertest1')

        print('done')