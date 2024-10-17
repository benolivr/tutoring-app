from django.urls import path
from .views import SignUpView, UpdateClassesView, test_view
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('add_hours/', views.add_hours, name='add_hours'),
    path('ta/<int:pk>/', views.ta_detail, name='ta_detail'),
    path('update-classes/', UpdateClassesView.as_view(), name='update_classes'),
    path("test/", test_view, name="test"),
]