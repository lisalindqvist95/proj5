import json

from rest_framework import generics, permissions
from proj5.permissions import IsOwnerOrReadOnly
from favourites.serializers import FavouriteSerializer
from django.contrib import auth
from django.http import HttpResponse
from django.views import View


class FavouriteList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavouriteSerializer

    def favourite_add(request, id):
        post = get_object_or_404(Post, id=id)
        if favourites.filter(id=request.user.id).exist():
            favourites.remove(request.user)
        else:
            favourites.add(request.user)
        return HttpResponseRedirect(request.Meta['HTTP_REFERER'])


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavouriteSerializer
