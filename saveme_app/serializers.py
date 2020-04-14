from rest_framework import serializers
from saveme_app.models import User, Missing, Shelter

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 모델 설정
        # fields = ('userEmail', 'userPw')  # 필드 설정
        fields = '__all__'


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'


class MissingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missing
        fields = '__all__'  # 모든 필드 사용
