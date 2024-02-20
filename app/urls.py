from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('meal', views.ViewSets_Meal)
router.register('rating', views.ViewSets_Rating)

urlpatterns = [
    path('viewsets/', include(router.urls)),
]
