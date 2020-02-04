from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.core.management import call_command


from faker import Faker


from students.models import Student


class StudentTestCase(TestCase):
    fake = Faker()
    # fixtures = ['db.json']

    def setUp(self):     # Запускается перед каждым тестом
        Student.objects.create(first_name='Leo', last_name='Ole', birth_date='2000-05-18',
                               email='qwe@gmail.com', telephone='123456789', address='Dnipro', group=None)

    def tearDown(self) -> None:     # Запускается после каждого теста
        pass

    @classmethod
    def setUpClass(cls):    # выполняется перед всеми тестами в классе
        call_command('loaddata', 'db.json', verbosity=0)

    @classmethod
    def tearDownClass(cls):    # выполняется после всех тестов в классе
        pass

    def test_student_has_attributes(self):
        student = Student.objects.get(first_name='Leo')
        self.assertEqual(student.get_info(), 'First Name: Leo, <br>Last Name: Ole, '
                                             '<br>Birth date: 2000-05-18, <br>Email: qwe@gmail.com, '
                                             '<br>Telephone: 123456789, <br>Address: Dnipro')

    def test_student_attribute_change_opportunity(self):
        student = Student.objects.get(first_name='Leo')
        student.first_name = 'john'
        student.last_name = 'silver'
        student.birth_date = '1000-05-18'
        student.email = 'ABC@gmail.com'
        student.telephone = '+159-987ewt54784'
        student.address = 'Minsk'
        student.save()
        self.assertEqual(Student.objects.get(first_name='John').get_info(),
                         'First Name: John, <br>Last Name: Silver, <br>Birth date: 1000-05-18, '
                         '<br>Email: abc@gmail.com, <br>Telephone: 15998754784, <br>Address: Minsk')

    def test_contact_is_valid(self):
        data = {
            'email': self.fake.email(),
            'subject': self.fake.word(),
            'text': self.fake.text()
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 302
        self.assertEqual(response.status_code, 302)    # то же самое, что тест выше

    def test_contact_is_valid_wrong_email(self):
        data = {
            'email': 'wrong_email',
            'subject': self.fake.word(),
            'text': self.fake.text()
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200

    def test_contact_is_valid_empty_subject(self):
        data = {
            'email': self.fake.email(),
            'subject': '',
            'text': self.fake.text()
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200
