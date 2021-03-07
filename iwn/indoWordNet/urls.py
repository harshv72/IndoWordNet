from django.conf.urls import url
from indoWordNet import views
urlpatterns = [
 url(r'^', views.HomePageView.as_view()),
]
