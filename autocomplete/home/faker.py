from faker import Faker
from .models import Names
fake = Faker()

def feed_db(n):
    for _ in range(n):
        Names.objects.create(
            name = fake.name()
        )
    