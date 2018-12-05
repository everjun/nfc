from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from coffee.models import Cup


class PaySerializer(serializers.Serializer):
    barcode = serializers.CharField(max_length=50)
    money = serializers.DecimalField(max_digits=10, decimal_places=2)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def save(self, **kwargs):
        if self.is_valid(raise_exception=True):
            res = Cup.objects.filter(barcode=self.validated_data['barcode']).update(
                balance=F('balance') + self.validated_data.get('money', 0))
            if res == 0:
                raise ValidationError(_('Wrong barcode'))
