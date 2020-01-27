from django.forms import ModelForm, Form, EmailField, CharField, ValidationError
from django.core.mail import send_mail
from django.conf import settings


import os


from students.models import Student, Group


class BaseStudentForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        #  filter(email=email) -> filter(email__exact=email)
        # email_exists = Student.objects.\
        #     filter(email__iexact=email).\
        #     exclude(email__iexact=self.instance.email)
        email_exists = Student.objects.\
            filter(email__iexact=email).\
            exclude(id=self.instance.id).\
            exists()
        # if Student.objects.filter(email__iexact=email).exclude(email__iexact=self.instance.email).exists():
        #     raise ValidationError(f'Email {email} is already used')
        if email_exists:
            raise ValidationError(f'Email {email} is already used')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if not telephone.isdigit():
            raise ValidationError(f'Telephone {telephone} consists consists not only from digits. '
                                  f'It should be introduced like this example: 123456789')
        telephone_exists = Student.objects.\
            filter(telephone=telephone).\
            exclude(id=self.instance.id)
        if telephone_exists.exists():
            raise ValidationError(f'Telephone {telephone} is already used')
        return telephone


class StudentsAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient_list)
        req_path = os.path.join(os.getcwd(), 'emails.txt')
        with open(req_path, 'a') as file:
            result = f'From: {email_from}, Subject: {subject}, message: {message}.'
            file.write(result)
