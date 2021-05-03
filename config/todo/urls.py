from django.urls import path
from .views import TodoCreateView
urlpatterns = [
    # path("", index, name="index")
    path("", TodoCreateView.as_view(), name="index")
]
