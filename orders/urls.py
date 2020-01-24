from django.urls import path, include
from .views import CreateOrderView, OrdersListView, OrderDeleteView, OrderRetrieveView

app_name = "orders"
urlpatterns = [
    path('', CreateOrderView.as_view()),  # POST
    path('users/<int:user_id>/', OrdersListView.as_view(), 'order_list_view'),  # GET
    path('<slug:order_uuid>/', OrderRetrieveView.as_view()),  # GET
    path('<slug:order_uuid>/', OrderDeleteView.as_view()),  # DELETE
    # path('<slug:order_uuid>/', OrderUpdateView.as_view())  # PUT

]
