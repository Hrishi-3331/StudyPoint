from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage),
    path('chemistry/', chemistry, name='chemistry'),
    path('maths/', maths, name='maths'),
    path('ss/', ss, name='ss'),
    path('cp/', cp, name='cp'),
    path('ee/', ee, name='ee'),
    path('em/', em, name='em'),
    path('ed/', ed, name='ed'),
    path('cs/', cs, name='cs'),
    path('physics/', physics, name='physics'),
    path('physicssem/', physicsstream, name='physicssem'),
    path('chemistrysem/', chemstream, name='chemistrysem')
]

