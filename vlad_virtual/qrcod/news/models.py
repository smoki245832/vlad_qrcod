from django.db import models
from django.urls import reverse


class News(models.Model):

	title = models.CharField(max_length=255, verbose_name='Наименование')
	content = models.TextField(blank=True, verbose_name='Контент')
	created_at = models.DateTimeField(verbose_name='Дата начала')
	updated_at = models.DateTimeField(verbose_name='Дата окончания')
	is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
	category = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name='Категория', blank=True)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фотография', blank=True)

	def __str__(self):

		return self.title

	class Meta:

		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'
		ordering = ['-created_at']

	def get_absolute_url(self):

		return reverse('view_news', kwargs={'news_id': self.pk})


class User1(models.Model):

	name = models.CharField(max_length=255, verbose_name='Имя', db_index=True)
	last_name = models.CharField(max_length=255, verbose_name='Фамилия', db_index=True)
	father_name = models.CharField(max_length=255, verbose_name='Отчество', db_index=True)
	news = models.ForeignKey('News', on_delete=models.PROTECT,  verbose_name='Меропреятие', null=True, blank=True)


	class Meta:

		verbose_name = 'Участник'
		verbose_name_plural='Участники'
		ordering = ['name', 'last_name', 'father_name']

	def __str__(self):

		return self.name


class Category(models.Model):

	title = models.CharField(max_length=255, verbose_name='Наименование категории', db_index=True)

	def get_absolute_url(self):

		return reverse('category', kwargs={'category_id': self.pk})

	class Meta:

		verbose_name = 'Категория'
		verbose_name_plural='Категории'
		ordering = ['title']

	def __str__(self):

		return str(self.title)
