# Create your views here.

from knox.models import AuthToken
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response

from saveme_app.models import Missing, Shelter, Community, NewsData
from saveme_app.serializers import UserSerializer, RegisterSerializer, LoginSerializer, MissingSerializer, \
    ShelterSerializer, CommunitySerializer, NewsDataSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()  # models.py의 User 클래스안에 모든것을 의미. 모든 데이터를 다 가져온다.
#     serializer_class = UserSerializer
#
#     # email 필터적용하는 코드
#     def get_queryset(self):
#         queryset = User.objects.all()
#         email = self.request.query_params.get('userEmail', None)
#         if email is not None:
#             queryset = queryset.filter(userEmail=email)
#         return queryset

# User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Register API (회원가입)
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        # if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
        #     body = {"message": "short field"}
        #     return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # save 코드로 인해 data 가 저장된다.
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })


# Login API (로그인)
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        # validated_data 로 계정 인증을 한다.
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
        })


class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer


class MissingViewSet(viewsets.ModelViewSet):
    # queryset = Missing.objects.all()
    queryset = Missing.objects.all().order_by('-id')  # 역순으로 데이터 정렬
    serializer_class = MissingSerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all().order_by('-id')
    serializer_class = CommunitySerializer


class NewsDataViewSet(viewsets.ModelViewSet):
    queryset = NewsData.objects.all()
    serializer_class = NewsDataSerializer
