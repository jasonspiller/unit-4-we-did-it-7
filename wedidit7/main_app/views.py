from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'index.html', {'members': members})

class Team:
	def __init__(self, name, gender, description, age):
		self.name = name
		self.gender = gender
		self.description = description
		self.age = age

members = [
	Team('Jason', 'male', 'JavaScript and CSS Guru', 42),
	Team('Wade', 'male', 'peaceful jokerster with an optimist outlook', 39),
	Team('Kat', 'female', 'pretty mom but not a mom at all', 22)
]