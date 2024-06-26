from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from webchat.views import MessageView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('webchat/', MessageView.as_view()),
]
