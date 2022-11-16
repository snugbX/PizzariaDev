from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def login_view(request):
	return render(request, "accounts/login.html")



def logout_view(request: HttpRequest) -> HttpResponse:
	...


def cria_usuario(request: HttpRequest) -> HttpResponse:
	...
