from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import ServerView, CategoryView, ServerMembershipView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('server/', ServerView.as_view()),
    path('category/', CategoryView.as_view()),
    path(r'membership/<int:server_id>/membership/', ServerMembershipView.as_view(), name='server_membership'),
]