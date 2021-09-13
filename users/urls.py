from django.urls import path
# from . import views
from .views import SignUpView, change_password

urlpatterns = [
        path('^password/', change_password, name='change_password'),
        path('signup/', SignUpView.as_view(), name='signup'),
]
