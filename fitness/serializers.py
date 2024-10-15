from rest_framework import serializers
from django.contrib.auth.models import User, authenticate
from .models import Activity, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user with the validated data.
        """
        user = User.objects.create_user(**validated_data)
        return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")
        attrs['user'] = user
        return attrs

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'activity_type', 'duration', 'distance', 'calories_burned', 'date']
        read_only_fields = ['user']  # User should not be provided in requests

        extra_kwargs = {
            'distance': {'required': False, 'allow_null': True}  # Allow null for non-distance activities
        }

    def create(self, validated_data):
        """
        Set the user before saving the Activity.
        """
        user = self.context['request'].user  # Get the user from the request context
        validated_data['user'] = user
        return super().create(validated_data)


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['user', 'total_activities', 'total_distance', 'total_calories_burned', 'month', 'year']
        read_only_fields = ['user']  # User should not be provided in requests
