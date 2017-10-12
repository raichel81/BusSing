from rest_framework import serializers
from routes.models import Routes #, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    routes = serializers.HyperlinkedRelatedField(many=True, view_name='route-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'routes')

class RouteSerializer(serializers.ModelSerializer):
    patterns = serializers.HyperlinkedRelatedField(many=True, read_only= True, view_name="pattern-detail")

    class Meta:
        model=Routes
        