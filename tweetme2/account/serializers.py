
from .models import Profile
from django.core import mail
from django.db.models.fields import EmailField
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage


# User Serializer
#Pillamos el usuario
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','first_name','last_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        #user.is__active= False
        connection = mail.get_connection()
        # Manually open the connection
        connection.open()
        emailtry = EmailMessage(
            'Activate your account',
            'Confirm your register',
            'tweetteadevelop@gmail.com',
            ['email'],
        )
        emailtry.fail_silently= False
        emailtry.send()
        connection.close()
         
        return user
    
    def validate(self, data):
        # Comprobamos que el correo no exista
        if User.objects.filter(email=data["email"]) == []:
            raise serializers.ValidationError("Email registered before")
            
        if  len(data['password']) < 8 :
            raise serializers.ValidationError("Password must have at least 8 characters")
        return data

        
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    following_count = serializers.SerializerMethodField('get_following')
    followers_count = serializers.SerializerMethodField('get_followers')
    def get_following(self,obj):
        return obj.followers.all().count()
    def get_followers(self,obj):
        return obj.following.all().count()
    class Meta:
        model = Profile
        fields = ('user','pub','bio', 'location','image','following_count','followers_count')
    
   