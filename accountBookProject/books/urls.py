from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import BookViewSet, Type1_ViewSet, Type2_ViewSet, Type3_ViewSet


book_router = SimpleRouter(trailing_slash=False)
book_router.register('books', BookViewSet, basename='books')

type1_router = SimpleRouter(trailing_slash=False)
type1_router.register('type1', Type1_ViewSet, basename='type1')

type2_router = SimpleRouter(trailing_slash=False)
type2_router.register('type2', Type2_ViewSet, basename='type2')

type3_router = SimpleRouter(trailing_slash=False)
type3_router.register('type3', Type3_ViewSet, basename='type3')

urlpatterns = [
    path('', include(book_router.urls)),
    path('books/<int:book_id>/', include(type1_router.urls)),
    path('books/<int:book_id>/', include(type2_router.urls)),
    path('books/<int:book_id>/', include(type3_router.urls)),
]