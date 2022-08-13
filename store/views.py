from rest_framework.generics import UpdateAPIView
from .models import Order
from .serializers import OrderSerializer


class OrderAPIUpdate(UpdateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	lookup_field = 'slug'
