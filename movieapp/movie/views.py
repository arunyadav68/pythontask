from django.shortcuts import render,redirect
from .models import movie
from .forms import MovieForm

# Create your views here.
def add_movies(request):
	
	form = MovieForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_movies')
	return render(request, "add_movie.html",{'form':form})

def list_movies(request):
	movies = movie.objects.all()
	return render(request, "list_movies.html",{'movies':movies})

def edit_movie(request,id):
	movies = movie.objects.get(id=id)
	form = MovieForm(request.POST or None, instance=movies)
	if form.is_valid():
		form.save()
		return redirect('list_movies')
	return render(request, "edit_movie.html",{'movie':movie,'form':form})

def delete_movie(request,id):
	movies = movie.objects.get(id=id)
	if request.method == "POST":
		movies.delete()
		return redirect('list_movies')
	return render(request, "delete_movie.html",{'movies':movies})