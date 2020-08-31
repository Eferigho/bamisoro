from django.urls import path
from . import views


urlpatterns = [
    # post views
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
