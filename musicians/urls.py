from django.urls import path
from . import views

urlpatterns = [
    path("", views.AddMusicianClassView.as_view(), name="add_musician"),
    path("edit/<int:id>", views.UpdateMusicianClass.as_view(), name="edit_musician"),
]
