from rest_framework.generics import get_object_or_404

from apps.staff.models import Staff


def get_staff(*, staff_iin):
    return get_object_or_404(Staff, iin=staff_iin)


def list_staff():
    return Staff.objects.all()
