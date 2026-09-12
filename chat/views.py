from django.shortcuts import redirect, render
from django.http import JsonResponse

from chat.models import Room,Message


# Create your views here.
def home(request):
    return render(request,'home.html')  
def room(request,room):
    username = request.GET.get('username','')
    room_details = Room.objects.get(name=room)
    return render(request,'room.html',{
        'room':room,
        'room_details': room_details,
        'username': username
            ### here we are getting the username from the url parameter that we passed in the checkview function and we are passing it to the room.html so that we can use it in the room.html to display the username of the user who sent the message.
        })
def checkview(request):
    room=request.POST['room_name']  ### here we are getting the name of the room that user will enter in the input field of home.html
    username=request.POST['username']  ### here we are getting the name of the user that user will enter in the input field of home.html
    if Room.objects.filter(name=room).exists():  ### here we are checking whether the room is already created or not...if it is created then we will enter the room otherwise we will create a new room and enter it.....
        return redirect('/'+room+'/?username='+username)  ### if it is created then we will enter the room and also pass the username as a parameter in the url so that we can use it in the room.html to display the username of the user who sent the message.
    else:
        new_room=Room.objects.create(name=room)  ### if it is not created then we will create a new room and enter it.....
        new_room.save()  ### save the new room in the database.
        return redirect('/'+room+'/?username='+username)  ### after creating the new room we will enter the room and also pass the username as a parameter in the url so that we can use it in the room.html to display the username of the user who sent the message.

def getMessages(request, room):
    room_obj = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room)
    return JsonResponse({
        'messages': list(messages.values())
    })

def send(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']
    
    room_obj = Room.objects.get(id=room_id)
    
    new_message = Message.objects.create(
        user=username,
        room=room_obj.name,
        value=message
    )
    new_message.save()
    
    return JsonResponse({'status': 'ok'})