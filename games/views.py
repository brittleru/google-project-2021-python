from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def games(request):
    return render(request, 'games/all_games.html', {})

def block_rain(request):
    return render(request, 'games/block_rain.html', {})

def breakout(request):
    return render(request, 'games/breakout.html', {})

def catcher(request):
    return render(request, 'games/catcher.html', {})

def dodge(request):
    return render(request, 'games/dodge.html', {})

def doodle_jump(request):
    return render(request, 'games/doodle_jump.html', {})

def fruit_ninja(request):
    return render(request, 'games/fruit_ninja.html', {})

def pac_man(request):
    return render(request, 'games/pac_man.html', {})

def sky_burger(request):
    return render(request, 'games/sky_burger.html', {})

def snake(request):
    return render(request, 'games/snake.html', {})

def space_invaders(request):
    return render(request, 'games/space_invaders.html', {})

def t_rex(request):
    return render(request, 'games/t_rex.html', {})
