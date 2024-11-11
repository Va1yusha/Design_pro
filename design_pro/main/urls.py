from django.urls import path
from .views import register_view, login_view, home_view, logout_view, create_request, view_requests, delete_request, change_status, view_all_requests

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('create_request/', create_request, name='create_request'),
    path('view_requests/', view_requests, name='view_requests'),
    path('delete_request/<int:request_id>/', delete_request, name='delete_request'),
    path('change_status/<int:request_id>/', change_status, name='change_status'),
    path('view_all_requests/', view_all_requests, name='view_all_requests'),
]