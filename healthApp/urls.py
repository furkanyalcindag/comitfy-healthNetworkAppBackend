
from django.urls import re_path,path
from healthApp.views.GeneralViews import GeneralApiView


app_name = 'healthApp'
urlpatterns = [
     path('deneme/', GeneralApiView.as_view()),
]