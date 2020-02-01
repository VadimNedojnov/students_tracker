from django.forms import ModelForm, ValidationError


from teachers.models import Teacher


class BaseTeacherForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects. \
            filter(email__iexact=email). \
            exclude(id=self.instance.id). \
            exists()
        if email_exists:
            raise ValidationError(f'Email {email} is already used')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if not telephone.isdigit():
            raise ValidationError(f'Telephone {telephone} consists consists not only from digits. '
                                  f'It should be introduced like this example: 123456789')
        telephone_exists = Teacher.objects. \
            filter(telephone=telephone). \
            exclude(id=self.instance.id)
        if telephone_exists.exists():
            raise ValidationError(f'Telephone {telephone} is already used')
        return telephone


class TeachersAddForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'telephone', 'email')
