from django.urls import path
from match import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
修正    path('players', views.PlayerList.as_view()),
    path('player/<int:id>/', views.PlayerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
