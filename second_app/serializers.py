from rest_framework import serializers
from .models import Movies,User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = [ 'title', 'type','storyline','duration','IMDB_rating','cast','starring','available_on','origin'] 
        # exclude = ['email','password']



    class MoviesSerializer(serializers.Serializer):
        # id = serializers.IntegerField(read_only=True)
        title = serializers.CharField(required=False, max_length=100)
        type = serializers.CharField(max_length=100)
        storyline = serializers.CharField(required=False,max_length=100)
        duration = serializers.DurationField()
        IMDB_rating = serializers.IntegerField()
        cast = serializers.CharField(required=False,max_length=100)
        starring = serializers.CharField(required=False,max_length=100)
        available_on = serializers.CharField(required=False,  max_length=100)
        origin = serializers.CharField(required=False, max_length=100)

      

# serializer class for creating token and accumalate user/client in it
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','password']



    class UserSerializer(TokenObtainPairSerializer):
        password = serializers.CharField()
        email = serializers.EmailField()
        name = serializers.CharField(max_length=100)