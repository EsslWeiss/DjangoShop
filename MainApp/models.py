from django.db import models


class Category(models.Model):

	name = models.CharField(max_length=255, verbose_name='Категория', db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True)

	class Meta:
		ordering = ('name', )
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


class Product(models.Model):

	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=255, db_index=True, verbose_name='Продукт')
	description = models.TextField(verbose_name='Описание')
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
	image = models.ImageField(verbose_name='Изображение')
	stock = models.PositiveIntegerField(verbose_name='Количество')
	available = models.BooleanField(default=False, verbose_name='Доступность')
	slug = models.SlugField(max_length=255, unique=True)
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

	class Meta:
		ordering = ('created_date', 'updated_date')
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
		index_together = (('id', 'slug'), )

	def __str__(self):
		return '({}){} - {}$'.format(self.name, 
			self.category.name, self.price)

		