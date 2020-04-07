from django.urls import path
from .views import add_movies,list_movies,edit_movie,delete_movie

urlpatterns = [
	path('movie/create', add_movies, name='add_movies'),
	path('', list_movies, name='list_movies'),
	path('movie/edit/<int:id>', edit_movie, name='edit_movie'),
	path('movie/delete/<int:id>', delete_movie, name='delete_movie'),
	
]