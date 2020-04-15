from django.urls import path
from .views import (
    FavoriteListAPIView,
    CreateDestroyAPIView,
    UserInfo,
)

urlpatterns = [
    path('save/or/del/<int:pk>/', CreateDestroyAPIView.as_view(), name='create-favorite'),
    path('list/<str:username>/', FavoriteListAPIView.as_view()),
    path('', UserInfo.as_view()),
]
