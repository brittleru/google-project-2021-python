from django.urls import path
from games import views

app_name = "games"

urlpatterns = [
    path('', views.games, name='games'),
    path('block_rain/', views.block_rain, name='block_rain'),
    path('breakout/', views.breakout, name='breakout'),
    path('catcher/', views.catcher, name='catcher'),
    path('dodge/', views.dodge, name='dodge'),
    path('doodle_jump/', views.doodle_jump, name='doodle_jump'),
    path('fruit_ninja/', views.fruit_ninja, name='fruit_ninja'),
    path('pac_man/', views.pac_man, name='pac_man'),
    path('sky_burger/', views.sky_burger, name='sky_burger'),
    path('snake/', views.snake, name='snake'),
    path('space_invaders/', views.space_invaders, name='space_invaders'),
    path('t_rex/', views.t_rex, name='t_rex'),
]
