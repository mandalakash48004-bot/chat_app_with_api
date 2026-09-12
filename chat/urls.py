
from django.urls import path , include

from chat import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('<str:room>/',views.room,name='room'), ### in case we need to enter the room that is already created...and when we enter the room we see all the messages....thats why we use str:room meamns we can write the name of the room and enter it.
    path('checkview',views.checkview,name='checkview'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
    path('send',views.send,name='send'),
    ### checkview is used to check whether the room is already created or not...
    # if it is created then we will enter the room otherwise we will create a new room and enter it.....
    # we want this because otherwise when we click enter the room we cant identify it....
    # the str:room helps to enter a room that is created already...but we cant check it...
    # even if we know it exist we have to reapetaedly write this in the search bar...
    #thats why to check and just enter the room without writing  it....we need checkview...
    # we also put this as action in the form of home.html as it will run this function from views to hceck.
    
]
