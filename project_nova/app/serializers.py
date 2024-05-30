from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    name = serializers.CharField()
    data = serializers.CharField()
