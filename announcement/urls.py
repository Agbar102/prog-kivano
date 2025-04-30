from django.urls import path

from announcement.views import AnnouncementListAPIView, AnnouncementUpdateAPIView
from category.urls import urlpatterns

urlpatterns = [
    path("list", AnnouncementListAPIView.as_view()),
    path("update", AnnouncementUpdateAPIView.as_view())
]
