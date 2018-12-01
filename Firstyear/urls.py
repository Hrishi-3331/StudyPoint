from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage),
    path('chemistry/', chemistry),
    path('maths/', maths),
    path('ss/', ss),
    path('cp/', cp),
    path('ee/', ee),
    path('em/', em),
    path('ed/', ed),
    path('cs/', cs),
    path('physics/', physics),
    path('physicssem/', physicsstream),
    path('chemistrysem/', chemstream)
]

