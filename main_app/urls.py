"""URLs."""
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('storyline/', views.storyline, name='storyline'),
    path('share/', views.share, name='share'),
    path('signin/', views.signin, name='signin'),
    path('share_url/', views.post_share, name='post_share'),
    path('team/', views.team, name='team'),
]
