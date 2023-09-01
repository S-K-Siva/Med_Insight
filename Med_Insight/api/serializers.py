from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,MyModel

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ImageSerializer(ModelSerializer):
    class Meta:
        model = MyModel
        fields = "__all__"
        


# class MyModelSerializer(serializers.ModelSerializer):

#     creator = serializers.ReadOnlyField(source='creator.username')
#     creator_id = serializers.ReadOnlyField(source='creator.id')
#     image_url = serializers.ImageField(required=False)

#     class Meta:
#         model = MyModel
#         fields = "__all__"







