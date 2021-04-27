from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    text = models.TextField('Текст')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    category = models.ForeignKey('categories.Category', models.CASCADE, related_name='stuff_category', null=True)
    rating = models.PositiveSmallIntegerField('Рейтинг', default=0, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, 'product_images')
    image = models.ImageField('Фото', upload_to='product_image')


class ProductMark(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='product_marks', null=True)
    user = models.ForeignKey('users.Profile', models.CASCADE, 'user_marks', null=True)
    mark = models.PositiveSmallIntegerField('Оценка', default=5)
    comment = models.TextField('Коментарий')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.comment