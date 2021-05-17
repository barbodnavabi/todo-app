from django.urls import path
from .views import TodoCreateView,Register
from django.contrib.auth import views
urlpatterns = [
    # path("", index, name="index")
    path("", TodoCreateView.as_view(), name="index"),
    path('accounts/register/', Register.as_view(),name="register"),
    path('accounts/login/',views.LoginView.as_view(),name='login'),
    path('accounts/logout/', views.LogoutView.as_view(),name='logout'),
]