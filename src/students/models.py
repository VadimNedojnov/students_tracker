from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from faker import Faker


'''
CREATE TABLE students_student (first_name varchar(20), ...);
'''


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    # add avatar TODO
    telephone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey('students.Group',
                              null=True, blank=True,
                              on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    user_logged_in = models.BooleanField(default=False)
    user_platform = models.CharField(max_length=30, null=True, blank=True)

    # def save(self, *args, **kwargs):    # Как работает пре сейв и пост сейв
        # pre_save
        # super().save(*args, **kwargs)
        # post_save

    def get_info(self):
        return f'First Name: {self.first_name}, <br>Last Name: {self.last_name}, ' \
               f'<br>Birth date: {self.birth_date}, <br>Email: {self.email}, ' \
               f'<br>Telephone: {self.telephone}, <br>Address: {self.address}'

    @classmethod
    def generate_student(cls):
        fake = Faker()
        student = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=fake.date_between(start_date="-30y", end_date="-17y"),
                      email=fake.email(),
                      telephone=''.join(i for i in fake.phone_number() if i.isdigit()),
                      address=fake.address()
                      )
        # student.save()
        return student
            # f"First Name: {student.first_name}; <br>Last Name: {student.last_name};" \
            #    f"<br>Birth date: {student.birth_date}; <br>Email: {student.email};" \
            #    f"<br>Telephone: {student.telephone}, <br>Address: {student.address}"

    def __str__(self):
        return f'ID: {self.id}, {self.full_name}'

    @property
    def full_name(self):
        return f'First Name: {self.first_name}, Last Name: {self.last_name}'


class Group(models.Model):
    name = models.CharField(max_length=20)
    students_count = models.CharField(max_length=5)
    students_with_grants_count = models.CharField(max_length=5)
    group_leader_name = models.ForeignKey('students.Student', null=True, blank=True,
                                          on_delete=models.CASCADE, related_name='group_leader_name')
    start_lessons_time = models.TimeField(null=True, blank=True)
    headman = models.ForeignKey('teachers.Teacher', null=True, blank=True, on_delete=models.CASCADE)

    def get_info(self):
        return f'Group Name: {self.name}, <br>Students count: {self.students_count}, ' \
               f'<br>Students with grants count: {self.students_with_grants_count}, ' \
               f'<br>Group leader name: {self.group_leader_name}, ' \
               f'<br>Start lessons time: {self.start_lessons_time}'

    @classmethod
    def generate_group(cls):
        fake = Faker()
        group = cls(name=fake.company(),
                    students_count=fake.random_int(min=10, max=35, step=1),
                    students_with_grants_count=fake.random_int(min=0, max=5, step=1),
                    group_leader_name=fake.name(),
                    start_lessons_time=fake.time(pattern="%H:00:00", end_datetime=None),
                    headman=fake.name()
                    )
        group.save()
        return f"Group Name: {group.name}; <br />Students count: {group.students_count};" \
               f"<br />Students with grants count: {group.students_with_grants_count}; " \
               f"<br />Group leader name: {group.group_leader_name}; " \
               f"<br />Start lessons time: {group.start_lessons_time}"

    def __str__(self):
        return f'ID: {self.id}, Group Name: {self.name}'
