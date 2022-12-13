from django.urls import path
from mysite import views

urlpatterns = [
    path("world/",views.HelloWorldView.as_view(),name="hello")
]