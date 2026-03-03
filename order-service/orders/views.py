from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OrderCreateSerializer

orders = []
id_counter = 1


class OrdersListCreateView(APIView):
    def get(self, request):
        return Response(orders, status=status.HTTP_200_OK)

    def post(self, request):
        global id_counter

        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = {
            "id": id_counter,
            "item": serializer.validated_data["item"],
            "quantity": serializer.validated_data["quantity"],
            "customerId": serializer.validated_data["customerId"],
            "status": "PENDING",
        }

        orders.append(order)
        id_counter += 1

        return Response(order, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    def get(self, request, id):
        order = next((o for o in orders if o["id"] == id), None)
        if order is None:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(order, status=status.HTTP_200_OK)
