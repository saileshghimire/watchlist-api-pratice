from django.urls import path,include
# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import MovieDetailAV, MovieListAV
from watchlist_app.api.views import WatchlistAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS
from rest_framework.routers import DefaultRouter

# function_view api call
# urlpatterns = [
#     path('list/', movie_list, name='movie_list'),
#     path('<int:id>', movie_details, name='movie-detail'),

# ]

# class based view

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list'),
    path('<int:id>/',WatchDetailAV.as_view(), name='movie-detail'),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:id>', StreamPlatformDetailAV.as_view(),name='stream-detail'),
    
    path('',include(router.urls)),

    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/reviews/', ReviewList.as_view(), name="review-list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
]

