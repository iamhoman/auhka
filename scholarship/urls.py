
from django.urls import path

from .views import ScholarshipIntro, PastScholarListView, CurrentScholarListView, ScholarDetailView, \
    Swire, Chevening, News_Application

app_name = 'scholarship'

urlpatterns = [
    path('', ScholarshipIntro.as_view(), name='intro'),
    path('intro/', ScholarshipIntro.as_view(), name='intro'),
    path('swire/', Swire.as_view(), name='swire'),
    path('chevening/', Chevening.as_view(), name='chevening'),
    path('past_list/', PastScholarListView.as_view(), name='past_list'),
    path('current_list/', CurrentScholarListView.as_view(), name='current_list'),
    path('scholar/<int:pk>/', ScholarDetailView.as_view(), name='scholar_detail'),
    path('news_application/', News_Application.as_view(), name='news_application'),
]