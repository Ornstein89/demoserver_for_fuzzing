import uuid, random, os
from datetime import datetime, timezone


from django.db import transaction

from dateutil.rrule import rrule, MONTHLY, DAILY, HOURLY, MO, TU, WE, TH, FR, SA
from faker import Faker

from mainapp.models import Staff, Book

fk = Faker()

def genStaff():
    for i in range(5):
        newStaff = Staff()
        newStaff.username = f'user{i}'
        if i==0:
            newStaff.is_superuser = True
        newStaff.first_name = f'Иван{i}'
        newStaff.last_name = f'Иванов{i}'
        newStaff.set_password(f'pass{i}')
        newStaff.save()


def genBooks():
    for i in range(50):
        newBook = Book()
        newBook.title  = f'Заглавие {i}'
        newBook.dateOfEntry = fk.date_between(start_date=datetime(2000,1,1), end_date=datetime(2025,1,1))
        newBook.author = f'Автор {i}'
        newBook.developerOrganization = f'Издательство {i}'
        newBook.revisionNumber = random.randint(1, 5)
        newBook.abstract = f'Аннотация {i}'
        newBook.save()


def genAllData():
    with transaction.atomic():
        genStaff()
        genBooks()


def clearAllData():
    with transaction.atomic():
        Staff.objects.all().delete()
        Book.objects.all().delete()