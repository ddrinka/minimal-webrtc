from django.urls import path

from . import views

urlpatterns = [
    path('camera/', views.camera, name='camera'),
    path('camera/<str:room_name>/qr', views.camera_qr, name='camera_qr'),
]
