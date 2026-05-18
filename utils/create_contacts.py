import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Category, Contact

    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        phone = fake.phone_number()
        
        d = fake.date_this_year()
        created_date = datetime(d.year, d.month, d.day, 12, 0, 0)
        
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )