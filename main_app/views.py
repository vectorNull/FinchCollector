from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, color, description, age):
    self.name = name
    self.color = color
    self.description = description
    self.age = age

finches = [
  Finch('Will', 'red', 'gentle', 3),
  Finch('Sammy', 'green', 'fiesty', 0),
  Finch('Bob', 'blue', 'legless', 4)
]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })