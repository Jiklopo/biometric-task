from django.db import models


class JobTextChoices(models.TextChoices):
    WAITER = 'WTR'
    CLEANER = 'CLN'
    COOK = 'CK'
    GUARD = 'GRD'


class GenderTextChoices(models.TextChoices):
    MALE = 'M'
    FEMALE = 'F'
    FIGHT_HELICOPTER = 'H'
    UNKNOWN = 'U'
