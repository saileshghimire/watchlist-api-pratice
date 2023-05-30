# from django.shortcuts import render
# from .models import *
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {'movies': list(movies.values())}
#     return JsonResponse(data)

 
# def movie_details(request,id):
#     movie = Movie.objects.get(id=id)
#     data = {
#         'name': movie.name,
#         'description' :movie.description,
#         'active' :movie.active
#     }
#     return JsonResponse(data)


