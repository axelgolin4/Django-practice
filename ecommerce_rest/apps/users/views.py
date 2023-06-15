from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.serializer import UserSerializer, UserListSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def user_view(request):
    
    #list
    if request.method == 'GET':
        # QuerySet
        users = User.objects.all().values('id','username', 'name', 'email', 'password')
        user_serializer = UserListSerializer(users, many = True) #Serializa y regresa varios reultados
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    #create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk = None):
    #Consulta
    user = User.objects.filter(id = pk).first()
    #Validacion
    if user:
    
        #retrive
        if request.method == 'GET':
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        #update
        elif request.method == 'PUT':
                user_serializer = UserSerializer(user, data= request.data)
                if user_serializer.is_valid():
                        user_serializer.save()
                        return Response(user_serializer.data, status=status.HTTP_200_OK)
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #delete
        elif request.method == 'DELETE':

                user.delete()
                return Response({'message':'Usuario Eliminado Correctamente'}, status=status.HTTP_200_OK)
        
    return Response({'message':'No se encontro al usuario'}, status=status.HTTP_400_BAD_REQUEST)
