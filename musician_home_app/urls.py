from django.urls import path
from . import views

urlpatterns = [path("", views.HomePageClassView.as_view(), name="home")]
