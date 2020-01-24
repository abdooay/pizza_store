from rest_framework import serializers
from .models import Order, OrderItem
from users.models import Customer


class CreateOrderItemSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.Serializer):
    order_items = CreateOrderItemSerializer(many=True, required=False)
    user_id = serializers.IntegerField()
    mobile_no = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=120)

    def create(self, validated_data):
        order_items = validated_data['order_items']
        customer_id = validated_data["user_id"]
        order = Order.objects.create_order(customer_id=customer_id, order_items=order_items)
        return order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderItem
        fields = ['pizza_name', 'pizza_price', 'item_count']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['uuid', 'creating_date', 'status', 'preparation_time', 'out_for_delivery_time', 'cancellation_time',
                  'order_total_time', 'customer_name', 'captain_name', 'order_items']
