from rest_framework import serializers
from routes.models import * #, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    routes = serializers.HyperlinkedRelatedField(many=True, view_name='route-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'routes')

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    patterns = serializers.HyperlinkedRelatedField(many=True, view_name='pattern-detail', read_only= True)

    class Meta:
        model=Routes
        field = '__all__'

class StopSerializer(serializers.HyperlinkedModelSerializer):
    patterns = serializers.HyperlinkedRelatedField(many=True, view_name='pattern2-detail', read_only= True)
    
    class Meta:
        model = Stops 
        field = '__all__'

class PatternSerializer(serializers.HyperlinkedModelSerializer):
    trips = serializers.HyperlinkedRelatedField(many=True, view_name='trip-detal', read_only= True)

    class Meta:
        model = Patterns
        field = '__all__'
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        field = '__all__'


        