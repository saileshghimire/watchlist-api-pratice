from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import WatchlistSeralizer, StreamPlatformSeralizer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from watchlist_app.api.permission import AdminOrReadOnly, ReviewUserOrReadOnly

# from rest_framework.decorators import api_view


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSeralizer(movies,many=True)
#         return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = MovieSeralizer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
        


# @api_view(['GET','PUT','DELETE'])    
# def movie_details(request,id):
#     if request.method  == 'GET':
#         try:
#             movies = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSeralizer(movies)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movies = Movie.objects.get(id=id)
#         serializer = MovieSeralizer(movies,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         movies = Movie.objects.get(id=id)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
   

class WatchlistAV(APIView):
    def get(self,request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSeralizer(movies, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchlistSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self,request,id):
        try:
            movie = Watchlist.objects.get(id=id)
        except Watchlist.DoesNotExit:
            return Response({'error':'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSeralizer(movie)
        return Response(serializer.data)
    def put(self,request,id):
        movie = Watchlist.objects.get(id=id)
        serializer = WatchlistSeralizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        movie = Watchlist.objects.get(id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSeralizer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSeralizer(watchlist)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer = StreamPlatformSeralizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

class StreamPlatformVS(viewsets.ModelViewSet):
        queryset = StreamPlatform.objects.all()
        serializer_class = StreamPlatformSeralizer


class StreamPlatformAV(APIView):
    def get(self,request):
        platform = StreamPlatform.objects.all()
        # serializer = StreamPlatformSeralizer(platform, many=True, context={'request':request}) #for hyperlinkedRelated field 
        serializer = StreamPlatformSeralizer(platform, many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class StreamPlatformDetailAV(APIView):
    def get(self,request,id):
        try:
            platform = StreamPlatform.objects.get(id=id)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Stream not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSeralizer(platform)
        return Response(serializer.data)
    def put(self,request,id):
        platform = StreamPlatform.objects.get(id=id)
        serializer = StreamPlatformSeralizer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        platform = StreamPlatform.objects.get(id=id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# Genric views
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self,request,*arg,**kwargs):
#         return self.list(request,*arg,**kwargs)
    
#     def post(self,request,*arg,**kwargs):
#         return self.create(request,*arg,**kwargs)
    

# class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# concrete view classes
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)
        # comming 4 line doesn't allow user to create more than 1 review 
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviwed this movie!")
        if watchlist.number_rating == 0:
            watchlist.avg_rating == serializer.validated_data['rating']
        else:    
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
            watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist,review_user = review_user)

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
