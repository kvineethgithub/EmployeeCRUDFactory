from django.urls import path, include
from .views import EmployeeViewSet, RegisterApi
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("emp-view", EmployeeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('api/register', RegisterApi.as_view()),
    path('api/token', views.obtain_auth_token)

]
