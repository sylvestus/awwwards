from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Profile,Post,User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profilePhoto','bio','contact')
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'project_image','description', 'url','user','profile')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']