# -*- coding: utf-8 -*-
from routes.models import *
from routes.serializers import *
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from routes.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RouteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Routes.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        route = self.get_object()
        return Response(route.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StopViewSet(viewsets.ModelViewSet):
    queryset = Stops.objects.all()
    serializer_class = StopSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        stop = self.get_object()
        return Response(stop.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PatternViewSet(viewsets.ModelViewSet):
    queryset = Patterns.objects.all()
    serializer_class = PatternSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        pattern = self.get_object()
        return Response(pattern.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        trip = self.get_object()
        return Response(trip.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


