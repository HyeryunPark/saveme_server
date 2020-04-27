from django.urls import path, include

from saveme_app.views import RegisterAPI, LoginAPI, UserAPI

app_name = 'saveme_app'
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
    path("auth/register/", RegisterAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
]
