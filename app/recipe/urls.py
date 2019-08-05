from django.urls import pathe, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tags', view.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
