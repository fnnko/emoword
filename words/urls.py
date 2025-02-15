from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_view, name='start'),
    path('select/', views.emotion_select_view, name="emotion_select"),
    path('message/<int:emotion_id>', views.message_view, name='quote'),

]
