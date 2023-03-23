from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]


















# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.index, name='index')
# ]

# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('articles/',ArticleList.as_view()),
#     path('articles/<int:id>', ArticleDetails.as_view()),
# ]
