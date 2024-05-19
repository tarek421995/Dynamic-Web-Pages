from django.urls import path
from . import views


app_name = 'video_app'
urlpatterns = [
    path('<int:pk>/', views.webpage_detail, name='webpage_detail'),

]
