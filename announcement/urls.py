from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from announcement import views
from announcement.views import ItemViewSet, RecallViewSet

router = DefaultRouter()

router.register(r"items", ItemViewSet)
router.register(r"recall", RecallViewSet)

urlpatterns = [
    path("", views.CreateItemAPIView.as_view()),
    path('', include(router.urls)),
]
