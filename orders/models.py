from django.db import models, transaction, IntegrityError
from menu.models import PizzaType
from users.models import Customer, Captain
from functools import reduce
import uuid

ORDER_STATUS = (('RECEIVED', 'Received'),
                ('PREPARING', 'Preparing'),
                ('OUT_FOR_DELIVERY', 'Out for delivery'),
                ('DELIVERED', 'Delivered'),
                ('CANCELLED', 'Cancelled'),)


class OrdersManager(models.Manager):
    def create_order(self, customer_id=None, order_items=None):

        try:
            customer = _get_customer(user_id=customer_id)

            transaction.set_autocommit(False)
            try:

                order = self.model.objects.create(customer=customer, customer_name=customer.name, status='RECEIVED')
                order_items_model = _get_order_items(order_items, order)
                total_order_preparation_time = _get_total_order_preparation_time(order_items_model)
                order.preparation_time = total_order_preparation_time
                order.save()
                OrderItem.objects.bulk_create(order_items_model)

            except Exception as ex:
                transaction.rollback()
                raise
            else:
                transaction.commit()
                return order

            finally:
                transaction.set_autocommit(True)
        except Exception as ex:
            return None

    def cancel_order(self, order_uuid=None):
        order = self.get(uuid=order_uuid)
        if order.status in ('RECEIVED', 'PREPARING'):
            order.status = 'CANCELLED'
            order.save()
            return order
        else:
            # TODO: this should raise certain type of exception instead of None
            return None


# Create your models here.
class Order(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    creating_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=ORDER_STATUS)
    preparation_time = models.IntegerField(null=True)
    out_for_delivery_time = models.DateTimeField(null=True)
    cancellation_time = models.DateTimeField(null=True)
    order_total_time = models.IntegerField(null=True)
    customer_name = models.CharField(max_length=120, null=True, blank=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.SET_NULL, null=True)
    captain_name = models.CharField(max_length=120, null=True, blank=True)
    captain = models.ForeignKey(to=Captain, on_delete=models.SET_NULL, null=True)

    objects = OrdersManager()

    def __str__(self):
        return f"{self.customer_name} {self.creating_date} {self.status}"


class OrderItem(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    pizza = models.ForeignKey(PizzaType, on_delete=models.SET_NULL, null=True)
    pizza_name = models.CharField(max_length=120)
    pizza_price = models.FloatField()
    preparation_time = models.IntegerField()
    item_count = models.IntegerField()
    Order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='order_items')


def _get_customer(user_id=None):
    try:
        return Customer.objects.get(id=user_id)
    except Customer.DoesNotExist:
        return None


def _get_order_items(order_items, order):
    """

    :param order_items:
    :return: Returns List of orderItems Object
    """
    items_uuids_dict = {oreder_item['id']: oreder_item['quantity'] for oreder_item in order_items}

    ordered_pizza_types = PizzaType.objects.filter(uuid__in=items_uuids_dict.keys())
    order_items = [
        OrderItem(pizza=pizza_type, pizza_name=pizza_type.pizza.name, pizza_price=pizza_type.price,
                  preparation_time=pizza_type.preparation_time, item_count=items_uuids_dict[pizza_type.uuid],
                  Order=order) for pizza_type in
        ordered_pizza_types]

    return order_items


def _get_total_order_preparation_time(order_items):
    # def calc_total(item1, item2):
    #     total = (item1.item_count * item1.preparation_time) + (item2.item_count * item2.preparation_time)
    #     return total
    #
    # total_order_time = reduce(
    #     calc_total,
    #     order_items)
    total_order_time = 20
    return total_order_time

# TODO: Can normalize the order and the status but should consider the performance
# class OrderStatus(models.Model):
#     order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
#     creation_date
