from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from album.forms import AlbumForm
from album.models import AlbumModel


# Create your views here.
# def add_album(req):
#     if req.method == "POST":
#         add_form = AlbumForm(req.POST)
#         if add_form.is_valid():
#             add_form.save()
#             return redirect("home")
#     else:
#         add_form = AlbumForm()
#     return render(req, "add_album.html", {"form": add_form})

# class based view
class AddAlbumClassView(CreateView):
    form_class = AlbumForm
    template_name = "add_album.html"
    success_url = reverse_lazy("home")


# def edit_album(req, id):
#     data = AlbumModel.objects.get(pk=id)
#     if req.method == "POST":
#         album = AlbumForm(req.POST, instance=data)
#         if album.is_valid():
#             album.save()
#             return redirect("home")
#     else:
#         album = AlbumForm(instance=data)
#     return render(req, "edit_album.html", {"form": album})

class UpdateAlbumClassView(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    pk_url_kwarg = "id"
    template_name = "edit_album.html"
    success_url = reverse_lazy("home")
   


# def delete_album(req, id):
#     data = AlbumModel.objects.get(pk=id)
#     data.delete()
#     return redirect("home")


class DeleteAlbumClassView(DeleteView):
    model = AlbumModel
    pk_url_kwarg = "id"
    template_name = "delete_album.html"
    success_url = reverse_lazy("home")