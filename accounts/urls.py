from django.urls import path
from .views import UserRegistrationView, UserLoginView
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, UserViewSet, GroupViewSet


router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)        # Регистрация UserViewSet
router.register(r'groups', GroupViewSet) 

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]