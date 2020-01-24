from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response

from users.models import Customer
from .serializers import CreateOrderSerializer, OrderSerializer
from .models import Order
from django.db.models import Q
from .models import PizzaType


# Create your views here.
class CreateOrderView(views.APIView):

    def post(self, request):
        order = CreateOrderSerializer(data=request.data)
        if not order.is_valid():
            return Response(order.errors)

        else:
            order.save()
            return_data = OrderSerializer(data=order)
            return_data.is_valid()
            return Response(return_data.data)


class OrderRetrieveView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        order_id = self.kwargs.get('order_uuid')
        return Order.objects.get(uuid=order_id)


class OrdersListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        status = self.request.query_params.get('status', None)
        # Todo: Need to check if I can short circuit the query
        queryset = Order.objects.filter(customer_id=user_id)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


#
# class OrderUpdateView(generics.UpdateAPIView):
#     serializer_class = OrderSerializer
#
#     # def put(self, request, *args, **kwargs):
#     #     serilaizer = self.get_serializer(request.data)
#
#     def get_object(self):
#         order_uuid = self.kwargs.get('order_uuid')
#         Order.objects.get(uuid=order_uuid)
#

class OrderDeleteView(views.APIView):
    def delete(self, request, order_uuid):
        cancelled_order = Order.objects.cancel_order(order_uuid=order_uuid)
        if cancelled_order is None:
            return Response("can't cancel order as its being prepared or already cancelled", status=400)
        return Response("ordered cancelled")
