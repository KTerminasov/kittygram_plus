from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
# Префикс r перед строкой определяет raw-строку (или r-строку, так короче).
# Такую строку система будет читать как простую последовательность символов,
# игнорируя escape-последовательности
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
