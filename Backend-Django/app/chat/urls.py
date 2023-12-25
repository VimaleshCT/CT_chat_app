from django.urls import path
from .views import messageAPIView

urlpatterns = [
     path('messages',messageAPIView.as_view())
]