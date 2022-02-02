from django.urls import path
from match import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.PlayerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
