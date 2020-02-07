from students_tracker.settings import *


CELERY_ALWAYS_EAGER = True
CELERY_TASK_ALWAYS_EAGER = True
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


MIGRATION_MODULES = {
    'auth': None,
    'contenttypes': None,
    'default': None,
    'sessions': None,

    'students': None,
    'teachers': None,
}