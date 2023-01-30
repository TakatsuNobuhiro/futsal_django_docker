from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from futsal_django.match import views

urlpatterns = [
    path('member', views.MemberList.as_view()),
    path('club', views.ClubList.as_view()),
    path('player/<int:id>/', views.PlayerDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
