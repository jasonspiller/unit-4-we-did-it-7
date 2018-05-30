from django.urls import path
from . import views

urlpatterns = [
		path('', views.index, name='index'),
		path('signup/', views.signup, name='signup'),
		path('<int:user_id>/', views.show, name='show'),
		path('post_url/', views.signup, name='signup'),
		path('profile/', views.profile, name='profile'),
  		path('storyline/', views.storylineview, name='Storyline'),
] 

