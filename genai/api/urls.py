from django.urls import path
from genai.api import views

urlpatterns = [
    path('image', views.gen_img, name='image-gen'),
]
