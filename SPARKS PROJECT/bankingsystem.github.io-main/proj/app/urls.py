from django.urls import path
from .views import usersList , transfermoney , payments


urlpatterns = [
    path('', usersList , name="userlist"),
    path('montrans', transfermoney , name="transfermoney"),
    path('history', payments , name="payments"),
]