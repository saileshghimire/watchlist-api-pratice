from rest_framework import serializers
# from watchlist_app.models import Movie
from watchlist_app.models import Watchlist, StreamPlatform, Review


# validators for validation 
# this can be done like this and line 25 also .just remove validators=[name_length] and 25 works fine
# def name_length(value):
#         if len(value) < 2:
#              raise serializers.ValidationError("Name is too short!")
        
# class MovieSeralizer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField(read_only=True)
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    # field level validation
    # def validate_name(self,value):
        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else: 
    #         return value   
    # object level validation
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("name and DEscription can't be same")
    #     else:
    #         return data
       
# Modelserializers
# class MovieSeralizer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
#     class Meta:
#         model = Movie
#         fields = '__all__'
#         # fields = ['id','name','description']
#         # OR
#         # exclude = ['active']

#     def get_len_name(self,object):
#         return len(object.name)

#         # field level validation
#     def validate_name(self,value):
        
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else: 
#             return value   
#     # object level validation
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and DEscription can't be same")
#         else:
#             return data

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ['watchlist']


class WatchlistSeralizer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Watchlist
        fields = '__all__'
  
class StreamPlatformSeralizer(serializers.ModelSerializer):
    watchlists = WatchlistSeralizer(many=True,read_only=True)
# nested relationship ,model.py relatred name must be same as here used name Eg: watchlists,
# if not error occurs.

   #gives name of all movie in that warchlist which above can't give abouve give "watchlists": [],only.
    # watchlists = serializers.StringRelatedField(many=True)

    # hyperlinked: it gives link as pervious gives name 
    # watchlists = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only =True,
    #     view_name='movie-detail',
    #     lookup_field='id'
    # )
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        

# class StreamPlatformSeralizer(serializers.HyperlinkedModelSerializer):
#     watchlists = WatchlistSeralizer(many=True,read_only=True)
#     class Meta:
#         model = StreamPlatform
#         fields = '__all__'
        