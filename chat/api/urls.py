from django.urls import  path,include
from chat.api import views

"""
router=DefaultRouter()
router.register('crud',views.RoomView,basename='Room')
router.register('crud1',views.MessageView,basename='Message')
"""
urlpatterns=[
    path('rooms/', views.RoomView.as_view(),name='Room'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='RoomDetail'),
    path('messages/', views.MessageView.as_view(),name='Message'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='MessageDetail'),
]