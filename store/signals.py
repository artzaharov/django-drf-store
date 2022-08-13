from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from store.models import Order
import requests


@receiver(post_save, sender=Order)
def order_api_request(sender, instance, **kwargs):
	order = {
		'slug': instance.slug,
		'status': instance.status_id,
		'warehouse': instance.warehouse_id,
		'store': 'Store 1'
	}
	headers = {
		'Authorization': f'Token {instance.warehouse.token}'
	}

	print(kwargs)
	if kwargs['created']:
		# CREATE WAREHOUSE RECORD
		try:
			requests.post(instance.warehouse.url, json=order, headers=headers)
		except Exception as ex:
			print(ex)
	else:
		# UPDATE EXISTING WAREHOUSE RECORD
		# URL for creating looks like: http://127.0.0.1:8001/api/v1/order/
		# We change it to Update URL pattern: http://127.0.0.1:8001/api/v1/order/{str:slug}/
		url = f'{instance.warehouse.url}{instance.slug}/'
		try:
			requests.put(url, json=order, headers=headers)
		except Exception as ex:
			print(ex)


@receiver(post_delete, sender=Order)
def order_api_delete(sender, instance, **kwargs):
	headers = {
		'Authorization': f'Token {instance.warehouse.token}'
	}
	# DELETE WAREHOUSE RECORD
	# URL for creating looks like: http://127.0.0.1:8001/api/v1/order/
	# We change it to Delete URL pattern: http://127.0.0.1:8001/api/v1/order/{str:slug}/
	url = f'{instance.warehouse.url}{instance.slug}/'
	try:
		requests.delete(url, json={'slug': instance.slug}, headers=headers)
	except Exception as ex:
		print(ex)
