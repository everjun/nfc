from rest_framework import serializers

from coffee.models import Cup


class CupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cup
        fields = '__all__'
