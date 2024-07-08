from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_album(request):
    if request.method =='POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form' : album_form})

def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)

    if request.method =='POST': # user sent POST request
        album_form = forms.AlbumForm(request.POST, instance=album)  # capture the user post data
        if album_form.is_valid(): # checking the post data validation
            album_form.save() # if data valid save in the database
            return redirect('homepage')  # redirect to the page 
    return render(request, 'add_album.html', {'form' : album_form})

def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')  # redirect to the page 
