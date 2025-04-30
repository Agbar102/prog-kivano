from django.shortcuts import render

from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     UpdateAPIView)

from announcement.models import Item
from announcement.serializers import AnnouncementSerializer


class AnnouncementListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementUpdateAPIView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = AnnouncementSerializer