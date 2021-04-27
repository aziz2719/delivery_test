from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='profile', null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    dob = models.DateField('Дата рождения', blank=True, null=True)
    avatar = models.ImageField('Изображение', upload_to='user_image/')
    phone = models.CharField('Номер телефона', max_length=30)
    address = models.CharField('Адрес', max_length=100)
    balance = models.PositiveIntegerField('Баланс', default=0)


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Stuff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='stuff', null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Courier(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='courier', null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    car = models.TextField('Описание машины', blank=True, null=True)

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'