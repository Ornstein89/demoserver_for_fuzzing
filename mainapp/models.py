import uuid, random, string

from django.db import models
from django.contrib.auth.models import Group, User, AbstractUser

# Create your models here.

class Staff(AbstractUser):

    """
    Расширение стандартного класса пользователя Django
    """
    RANK_CHOISES = ()
    uuid = models.UUIDField(
        unique=True, blank=False, null=False, default=uuid.uuid4, editable=False)
    

class Book(models.Model):

    ### ПОЛЯ МОЖНО НАСЛЕДОВАТЬ НАСЛЕДУЮТСЯ ОТ КЛАССА NODE
    uuid = models.UUIDField(
        unique=True, blank=False, null=False, default=uuid.uuid4, editable=False)
    title = models.CharField(
        verbose_name='Название документа',max_length=256, null=False, blank=False)    
    abstract = models.TextField(
        verbose_name='Аннотация',
        max_length=1024, null=True, blank=True) # TODO для экономии места - в отдельную таблицу, чтобы наличие аннотации было бы опциональным

    dateOfEntry = models.DateField(
        verbose_name='Дата издания',
        blank=False, null=False)
    author = models.CharField(
        verbose_name='Авторы',
        max_length=256, null=True, blank=True)
    developerOrganization = models.CharField(
        verbose_name='Издатель',
        max_length=256, null=True, blank=True)
    revisionNumber = models.SmallIntegerField(
        verbose_name='Номер редакции', null=True, blank=True)

