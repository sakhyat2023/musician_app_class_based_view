from django.shortcuts import render
from django.views.generic import ListView
from album.models import AlbumModel

# Create your views here.
# def home_page(req):
#     posts = AlbumModel.objects.all()
#     return render(req, "index.html", {"posts": posts})

# class based view
class HomePageClassView(ListView):
    model = AlbumModel
    context_object_name = "posts"
    template_name = "index.html"