from rest_framework import serializers

from announcement.models import *

class SubItemSerializers(serializers.Serializer):
    sub_category = serializers.CharField()

class ItemViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class RecallViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recall
        fields = '__all__'



