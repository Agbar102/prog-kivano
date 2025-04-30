from rest_framework import serializers

from announcement.models import *

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"