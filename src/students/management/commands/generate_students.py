from django.core.management.base import BaseCommand


from students.models import Student, Group
from teachers.models import Teacher


import random
from faker import Faker


class Command(BaseCommand):
    help = 'This command generates 100 random students and adds them to the DB'

    # def handle(self, *args, **options):
    #     added_students = '\n---------------------------\n'.join(
    #         Student.generate_student() for i in range(100)).replace("<br />", "\n")
    #     return f'100 students successfully added to DB: {added_students}'

    # def handle(self, *args, **options):
    #     Group.objects.all().delete()
    #     Student.objects.all().delete()
    #     groups = [Group.objects.create(name=f'name_{i}') for i in range(10)]
    #
    #     number = int(options.get('number') or 100)
    #     for _ in range(number):
    #         student = Student.generate_student()
    #         student.group = random.choice(groups)
    #         student.save()

    def handle(self, *args, **options):
        fake = Faker()
        i = random.randint(1, 100000)
        group = Group.objects.create(name=f'name_{i}')
        teacher = Teacher.objects.create(first_name=fake.first_name(), last_name=fake.last_name())
        number = int(options.get('number') or 10)
        generated_students = []
        for _ in range(number):
            student = Student.generate_student()
            generated_students.append(student)
            student.group = group
            student.save()
        group.group_leader_name = random.choice(generated_students)
        group.headman = teacher
        group.save()

