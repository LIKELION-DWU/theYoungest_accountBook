from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import BookViewSet, TypeViewSet

book_router = SimpleRouter(trailing_slash=False)
book_router.register('books', BookViewSet, basename='books')

type_router = SimpleRouter(trailing_slash=False)
type_router.register('types', TypeViewSet, basename='types')

urlpatterns = [
    path('', include(book_router.urls)),
    path('books/<int:book_id>/', include(type_router.urls)),
]
