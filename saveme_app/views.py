from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from saveme_app.models import User, Missing, Shelter
from saveme_app.serializers import UserSerializer, MissingSerializer, ShelterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # models.py의 User 클래스안에 모든것을 의미. 모든 데이터를 다 가져온다.
    serializer_class = UserSerializer

    # email 필터적용하는 코드
    def get_queryset(self):
        queryset = User.objects.all()
        email = self.request.query_params.get('userEmail', None)
        if email is not None:
            queryset = queryset.filter(userEmail=email)
        return queryset


class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer


class MissingViewSet(viewsets.ModelViewSet):
    queryset = Missing.objects.all()
    serializer_class = MissingSerializer
