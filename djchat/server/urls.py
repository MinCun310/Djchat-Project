from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import ServerView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('server/category', ServerView.as_view())
]