from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_endpoints),
    path("api/patterns", views.get_patterns, name="get_patterns"),
    path("api/patterns/<str:id>", views.single_pattern, name="get_single_pattern"),
    path("api/users", views.get_users, name="get_users"),
    path("api/users/<str:id>", views.get_single_user, name="get_single_user"),
    path('api/users/<str:username>/patterns',views.get_patterns_by_username, name='get_patterns_by_username'),
    path("api/auth", views.get_test, name='auth_get_test'),
    path("api/comments", views.get_comments, name="get_comments"),
    path("api/comments/<str:id>", views.single_comment, name="delete_single_pattern"),
]
