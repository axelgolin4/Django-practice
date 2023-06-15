from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = '__all__'
        
        def create(self, validated_data):
                user = User.objects.create(**validated_data)
                user.set_password(validated_data['password'])
                user.save()
                return user
        def update(self, instance, validated_data):
                update_user = super().update(instance, validated_data)
                update_user.set_password(validated_data['password'])
                update_user.save()
                return update_user
        
class UserListSerializer(serializers.ModelSerializer):
        class Meta:
                model = User

        def to_representation(self, instance):
                return {
                        'id': instance['id'],
                        'username': instance['username'],
                        'name': instance['name'],
                        'email': instance['email'],
                        'password': instance['password']
                }
        





































'''
class TestUserSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=200)
        email = serializers.EmailField()

        def validate_name(self, value):
                #Costom Validation
                print(value)
                return value

        def validate_email(self, value):
                #Costom Validation    
                if value == '':
                        raise serializers.ValidationError("El email no puede estar vacio")
                return value

        def validate(self, data):
                if data['name'] in data['e|mail']:
                        raise serializers.ValidationError("El email no puede contener el nombre")
                return data
        
        def create(self, validated_data):
                return User.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
                instance.name = validated_data.get('name', instance.name)
                instance.email = validated_data.get('email', instance.email)
                instance.save()
                return instance
'''

