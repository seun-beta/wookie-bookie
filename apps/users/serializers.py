from rest_framework import serializers

from apps.users.models import User


class RegisterUserSerializer(serializers.ModelSerializer):

    """Serializer for user registration by username and password
    and initial One-Time-Password(OTP) generation"""

    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "author_pseudonym",
            "first_name",
            "last_name",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("password fields don't match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        return user
