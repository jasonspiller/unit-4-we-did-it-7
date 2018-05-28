"""Main App URLs."""
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD:wedidit7/main_app/urls.py
		path('', views.index, name='index'),
		path('signup/', views.signup_view, name='signup'),
]
=======
    path('', views.index, name='index'),
]
>>>>>>> master:main_app/urls.py
