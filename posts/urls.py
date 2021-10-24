from django.urls import path
from .views import (
    HomePageView,
    MessagesPageView,
    MessageDetailView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='Home'),
    path('newmessages/', MessagesPageView.as_view(), name='Messages'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),

]
