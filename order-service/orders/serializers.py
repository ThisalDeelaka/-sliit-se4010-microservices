from rest_framework import serializers


class OrderCreateSerializer(serializers.Serializer):
    item = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField(min_value=1)
    customerId = serializers.CharField(max_length=100)


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    item = serializers.CharField()
    quantity = serializers.IntegerField()
    customerId = serializers.CharField()
    status = serializers.CharField()
