from django.db import IntegrityError
from rest_framework import serializers
from pins.models import Pin


class PinSerializer(serializers.ModelSerializer):
    """
    Serializer for the Pin model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Pin
        fields = ['id', 'created_at', 'owner', 'post']

    def create(validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
