from .models import Student
from faker import Faker

fake = Faker()

def generate_random_data(n=10):
    try:
        for _ in range(n):
            Student.objects.create(
                name=fake.name(),
                age=fake.random_int(min=18, max=30),
                address=fake.address(),
                father_name=fake.name()
            )
        return f"Generated {n} random students successfully!"
    except Exception as e:
        return f"Error generating random data: {str(e)}"