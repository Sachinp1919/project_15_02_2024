from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from whatsapp.views import WhatsappViewSet

router = DefaultRouter()
router.register('whatsapp', WhatsappViewSet, basename='whatsapp')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls))
]
