from django.db import models


class Status(models.Model):
	title = models.CharField(max_length=255, verbose_name='Status')

	class Meta:
		verbose_name_plural = 'Statuses'

	def __str__(self):
		return self.title


class Warehouse(models.Model):
	title = models.CharField(max_length=255, verbose_name='Name')
	url = models.CharField(max_length=255, verbose_name='API URL')
	token = models.CharField(max_length=100, verbose_name='Token')

	def __str__(self):
		return self.title


class Order(models.Model):
	slug = models.SlugField(max_length=255, unique=True, verbose_name='Order number')
	status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Status')
	warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, verbose_name='Warehouse')

	def __str__(self):
		return self.slug
