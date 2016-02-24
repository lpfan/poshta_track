from rest_framework import serializers


class ParselSerializer(serializers.Serializer):
    eventdescription = serializers.CharField()
    lastofficeindex = serializers.CharField()
    lastoffice = serializers.CharField()
    code = serializers.CharField()
