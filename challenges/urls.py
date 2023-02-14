from django.urls import path
from . import views
urlpatterns =[
    path("",views.index,name="index"),
    path("<int:month>",views.challNum),
    path("<str:month>",views.chall,name="month_path")
]