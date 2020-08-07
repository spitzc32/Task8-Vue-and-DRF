from rest_framework import serializers
from profiles.models import Profile, ProfileStatus

"""
Task 4: Serializers
Using ModelSerializer to get the properties of our Models (Applying DRY Principle)
Solutions derived from excercises.
"""

class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("avatar",)


class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"   
