from django.urls import path, include
from .views import BookList, BookDetail, AuthorList, AuthorDetail, AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('', include(router.urls))
]