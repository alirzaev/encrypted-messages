from django.urls import path

from .views import MessageCreateView, MessageDecryptView

urlpatterns = [
    path('', MessageCreateView.as_view(), name='index'),
    path('<int:pk>/', MessageDecryptView.as_view(), name='message_decrypt'),
]
