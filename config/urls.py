from django.contrib import admin
from django.urls import path,include
from app.views import CompanyView, BuildingView, AreaView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('company', CompanyView)
router.register('building', BuildingView)
router.register('area', AreaView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]