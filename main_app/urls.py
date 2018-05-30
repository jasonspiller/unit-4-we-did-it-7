"""URLs."""
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('signup/', views.signup, name='signup'),
    # path('<int:user_id>/', views.show, name='show'),
    # path('post_url/', views.signup, name='signup')
]
