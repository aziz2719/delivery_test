from django.db import models

class Category(models.Model):
    category = models.CharField('Категория', max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'