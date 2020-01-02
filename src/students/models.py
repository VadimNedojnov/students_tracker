from random import randint


from django.db import models
from faker import Faker


'''
CREATE TABLE students_student (first_name varchar(20), ...);
'''


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)    #clear phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

    def det_info(self):
        return f'{self.first_name}, {self.last_name}, {self.birth_date}, {self.email}, ' \
               f'{self.telephone}, {self.address}'

    @classmethod
    def generate_student(cls):
        fake = Faker()
        first_last_name = fake.name().split(" ")
        student = cls(first_name=first_last_name[0],
                      last_name=first_last_name[1],
                      birth_date=fake.date_between(start_date="-30y", end_date="-17y"),
                      email=fake.email(),
                      telephone=randint(100000000, 99999999999),
                      address=fake.address()
                      )
        student.save()
        return f"<br />First Name: {student.first_name}; <br />Last Name: {student.last_name};" \
               f"<br />Birth date: {student.birth_date}; <br />Email: {student.email};" \
               f"<br />Telephone: {student.telephone}, <br />Address: {student.address}"


class Group(models.Model):
    group_name = models.CharField(max_length=20)
    students_count = models.CharField(max_length=5)
    students_with_grants_count = models.CharField(max_length=5)
    group_leader_name = models.CharField(max_length=20)
    start_lessons_time = models.TimeField()

    def det_info(self):
        return f'{self.group_name}, {self.students_count}, {self.students_with_grants_count}, ' \
               f'{self.group_leader_name}, {self.start_lessons_time}'
