from django.db import models


class JobChoices(models.TextChoices):
    WAITER = 'WTR'
    CLEANER = 'CLN'
    COOK = 'CK'
    GUARD = 'GRD'


class GenderChoices(models.TextChoices):
    MALE = 'M'
    FEMALE = 'F'
    FIGHT_HELICOPTER = 'H'
    UNKNOWN = 'U'
