from django.urls import path
from .views import ReactView
from .import views
urlpatterns = [
    # path("wel/", ReactView.as_view(), name="reactview"),
    path('', views.ReactViewFunction, name="welcome"),
    path('wel/', ReactView.as_view(), name="wel")
]
