from django.urls import path

from . import views

urlpatterns = [
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("cria_usuario", views.cria_usuario, name="cria_usuario"),
]