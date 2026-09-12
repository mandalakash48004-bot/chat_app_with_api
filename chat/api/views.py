from .serializers import RoomSerializers,MessageSerializers
from chat.models import Room,Message
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class RoomView(generics.ListCreateAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializers
    authentication_classes = [SessionAuthentication]

    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name']  # Specify the fields you want to filter on

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializers    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class MessageView(generics.ListCreateAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializers 
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date','room']
    

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializers     
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination


#################################################################################################################################
# SUMMARY OF IMPLEMENTING API IN A PROJCT.
# # 1) WHY DO WE NEED AN API?
#
# We can create, read, update, and delete data using a web browser.
# However, a browser is only one way to use our project.
#
# An API allows other applications to communicate with our Django project.
# For example:
# - A mobile chat application can use our chat data.
# - A React or Angular frontend can use our backend.
# - Another website can read or send chat messages.
# - Different programs can share data automatically.
#
# The browser shows HTML pages, but an API usually sends data in JSON format.
# JSON is easy for computers and mobile applications to understand.
#
# Therefore, an API makes our project more useful, reusable, and flexible.


# 2) HOW DO WE ADD AN API TO OUR PROJECT?
#
# We use Django REST Framework, also called DRF.
#
# The basic process is:
# 1. Create a serializer to convert Django model objects into JSON.
# 2. Create API views to handle requests.
# 3. Create API URLs so users can access the views.
# 4. Add the API URLs to the main project URLs.
#
# A user can then visit addresses such as:
#
# /api/rooms/
# /api/messages/
#
# These addresses allow applications to read or create rooms and messages.


# 3) WHAT EXTRA FILES DO WE NEED AND WHY?
#
# Inside the chat app, we create an api folder.
#
# chat/api/__init__.py
# This tells Python that the api folder is a Python package.
#
# chat/api/serializers.py
# This converts model data into JSON.
# It also converts incoming JSON data into Django model objects.
#
# chat/api/views.py
# This contains the logic for the API.
# It decides what should happen when someone sends a GET, POST,
# PUT, PATCH, or DELETE request.
#
# chat/api/urls.py
# This connects API addresses to API views.
#
# We also update:
#
# djangochat/settings.py
# We add Django REST Framework and django-filter to INSTALLED_APPS.
# We can also add default API settings here.
#
# djangochat/urls.py
# We connect the API URLs to the main project using:
#
# path('api/', include('chat.api.urls'))
#
# The models.py file normally does not need changes if our models
# already contain the required data.


# 4) WHAT CODE DO WE WRITE?
#
# serializers.py:
#
# from rest_framework import serializers
# from chat.models import Room, Message
#
# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = ['name']
#
# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = ['value', 'date', 'user', 'room']
#
# The serializers convert Room and Message objects into JSON data.
#
#
# views.py:
#
# from rest_framework import generics
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from chat.models import Room, Message
# from .serializers import RoomSerializer, MessageSerializer
#
# class RoomView(generics.ListCreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['name']
#     search_fields = ['name']
#
# class MessageView(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['user', 'room']
#     search_fields = ['user', 'room']
#
# ListCreateAPIView gives us:
# GET    -> view a list of objects
# POST   -> create a new object
#
# For a complete CRUD API, detail views are also used:
#
# class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#
# This gives us:
# GET    -> view one room
# PUT    -> replace a room
# PATCH  -> partially update a room
# DELETE -> delete a room
#
#
# api/urls.py:
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('rooms/', views.RoomView.as_view()),
#     path('rooms/<int:pk>/', views.RoomDetailView.as_view()),
#     path('messages/', views.MessageView.as_view()),
#     path('messages/<int:pk>/', views.MessageDetailView.as_view()),
# ]
#
# djangochat/urls.py:
#
# from django.urls import path, include
#
# urlpatterns = [
#     path('api/', include('chat.api.urls')),
# ]
#
# settings.py:
#
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'django_filters',
# ]
#
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend'
#     ],
# }
#
# SearchFilter must also be added in the API view if we want searching
# with a query such as:
#
# /api/rooms/?search=classroom
#
# Exact filtering can be used like this:
#
# /api/rooms/?name=classroom
#
# /api/messages/?user=Akash
#
# Note: If SEARCH_PARAM is set to 'q' in settings.py, searching uses:
#
# /api/rooms/?q=classroom
#
# Otherwise, DRF normally uses:
#
# /api/rooms/?search=classroom


# 5) WHAT IS THE RESULT?
#
# After adding the API, we can open these URLs:
#
# /api/rooms/
# /api/rooms/1/
# /api/messages/
# /api/messages/1/
#
# The API displays data in JSON format and also provides a browsable page
# where we can test GET, POST, PUT, PATCH, and DELETE requests.
#
# For example, the rooms API may return:
#
# {
#     "name": "Python Room"
# }
#
# The messages API may return:
#
# {
#     "value": "Hello",
#     "date": "2026-09-03T10:30:00Z",
#     "user": "Akash",
#     "room": "Python Room"
# }
#
# The final result is that our chat project can still work in a browser,
# but it can also communicate with mobile apps, frontend frameworks,
# and other computer programs.
#
# In simple words:
# A normal Django page is mainly made for people.
# An API is mainly made for programs.
# Using both makes our project more powerful.    