from django.urls import path

from .views import OrderDetailView, OrdersListCreateView

urlpatterns = [
    path("orders", OrdersListCreateView.as_view(), name="orders-list-create"),
    path("orders/<int:id>", OrderDetailView.as_view(), name="orders-detail"),
]
