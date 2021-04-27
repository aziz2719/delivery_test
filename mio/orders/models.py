from django.db import models
from django.db.models import F, Sum
from products.models import Product
from decimal import Decimal 


class Order(models.Model):
    CHOICES = (
        ('N','New courier appointed'),#новый курьер назначен
        ('T','The manager looked at the order and appointed a courier'),#менеджер посмотрел заказ и назнач нов курьера
        ('O','On my way'),#в пути
        ('D','Delivered'),#доставлено
        ('С','Сanceled'),#отменен
    )
    customer = models.ForeignKey('users.Profile', models.SET_NULL, related_name='customer_order', null=True)
    courier = models.ForeignKey('users.Courier', models.SET_NULL, related_name='courier_order', null=True)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    total_price = models.DecimalField('Цена', max_digits=10, decimal_places=0, default=0, blank=True, null=True)
    address = models.CharField('Адрес доставки', max_length=255)
    status = models.CharField(max_length=100, choices=CHOICES)

    def set_total_price(self):
        self.total_price = self.prodect_order_product.all().aggregate(total_price=Sum(F('good_quantity') * F('product__price')))['total_price']
        self.save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, null=True)
    order = models.ForeignKey(Order, models.CASCADE, 'prodect_order_product', null=True)
    good_quantity = models.PositiveSmallIntegerField('Количество товара', default=1) 

    class Meta:
        verbose_name = 'Заказ продукта'
        verbose_name_plural = 'Заказ продуктов'