from django.urls import path
from basic_app import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name='user_login'),
    path('user_profile/', views.profile_page, name="user_profile"),
]
