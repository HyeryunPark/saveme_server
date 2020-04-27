from rest_framework import serializers

from saveme_app.models import Missing, Shelter
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Serializer 란?
#   복잡한 데이터를 쿼리셋 및 모델 인스턴스로 쉽게 변환 시키고,
#   이를 파이썬 데이터 타입에 맞춰 쉽게 렌더링 할 수 있게 해주는 것

# DRF Serializer 에는 어떤 것들이 있는가
#   BaseSerializer, ListSerializer, ModelSerializer

# 언제 쓰는가

# 어떻게 쓰는가
# ModelSerializer + viewset
# BaseSerializer + api_view

# 뭐때문에 쓰는가
# ModelSerializer
#   depth
# BaseSerializer
#   to_representation()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 모델 설정
        fields = ('id', 'username', 'email')  # 필드 설정
        # fields = '__all__'


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 모델 설정
        fields = ('id', 'username', 'email', 'password')  # 필드 설정
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password']
        )
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'


class MissingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missing
        fields = '__all__'  # 모든 필드 사용
