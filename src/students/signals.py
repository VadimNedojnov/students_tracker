from django.db.models.signals import pre_save
from django.dispatch import receiver
from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.telephone = ''.join(i for i in instance.telephone if i.isdigit())
    converted_first_name = instance.first_name.split(' ')
    instance.first_name = ' '.join(i[0].upper() + i[1:] for i in converted_first_name)
    if '-' in instance.last_name:
        converted_last_name = instance.last_name.split('-')
        instance.last_name = '-'.join(i[0].upper() + i[1:] for i in converted_last_name)
    elif ' ' in instance.last_name:
        converted_last_name = instance.last_name.split(' ')
        instance.last_name = ' '.join(i[0].upper() + i[1:] for i in converted_last_name)
    else:
        instance.last_name = instance.last_name[0].upper() + instance.last_name[1:]
