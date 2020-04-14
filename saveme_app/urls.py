from django.urls import path, include

app_name = 'saveme_app'
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
]