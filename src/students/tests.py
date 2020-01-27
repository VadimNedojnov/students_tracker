from django.test import TestCase


from students.models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(first_name='Leo', last_name='Ole', birth_date='2000-05-18',
                               email='qwe@gmail.com', telephone='12345678', address='Dnipro', group=None)

    def test_student_has_attributes(self):
        student = Student.objects.get(first_name='Leo')
        self.assertEqual(student.get_info(), 'First Name: Leo, <br>Last Name: Ole, '
                                             '<br>Birth date: 2000-05-18, <br>Email: qwe@gmail.com, '
                                             '<br>Telephone: 12345678, <br>Address: Dnipro')

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
