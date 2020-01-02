from django.core.management.base import BaseCommand


from students.models import Student


class Command(BaseCommand):
    help = 'This command generates 100 random students and adds them to the DB'

    def handle(self, *args, **options):
        added_students = '\n---------------------------\n'.join(
            Student.generate_student() for i in range(100)).replace("<br />", "\n")
        return f'100 students successfully added to DB. <br />{added_students}'
