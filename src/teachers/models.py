from random import randint
from random import choice


from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)    # clear phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=20)
    experience = models.CharField(max_length=3)

    def get_info(self):
        return f'First Name: {self.first_name}, <br>Last Name: {self.last_name}, <br>Birth date: {self.birth_date},' \
               f'<br>Email: {self.email}, <br>Telephone: {self.telephone}, <br>Address: {self.address}, ' \
               f'<br>Subject: {self.subject}, <br>Working experience: {self.experience}'

    @classmethod
    def generate_teacher(cls):
        fake = Faker()
        sequence = ['math', 'physics', 'chemistry', 'sport', 'literature', 'foreign language']
        teacher = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=fake.date_between(start_date="-60y", end_date="-30y"),
                      email=fake.email(),
                      telephone=fake.phone_number(),
                      address=fake.address(),
                      subject=choice(sequence),
                      experience=randint(0, 10)
                      )
        teacher.save()
        return f"First Name: {teacher.first_name}; <br>Last Name: {teacher.last_name};" \
               f"<br>Birth date: {teacher.birth_date}; <br>Email: {teacher.email};" \
               f"<br>Telephone: {teacher.telephone}; <br>Address: {teacher.address};" \
               f"<br>Subject: {teacher.subject}; <br>Working experience: {teacher.experience}"
