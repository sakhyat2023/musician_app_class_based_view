from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.AddAlbumClassView.as_view(), name="add_album"),
    path("edit/<int:id>", views.UpdateAlbumClassView.as_view(), name="edit_album"),
    path("delete/<int:id>", views.DeleteAlbumClassView.as_view(), name="delete_album"),
]
