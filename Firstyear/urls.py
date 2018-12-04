from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage),
    path('chemistry/', chemistry, name='chemistry'),
    path('maths/', maths, name='maths'),
    path('ss/', ss, name='ss'),

    # CP
    path('cp/', cp, name='cp'),
    path('cp/assignments', cp_ass, name='cp_assignments'),
    path('cp/notes', cp_notes, name='cp_notes'),
    path('cp/ebooks', cp_ebooks, name='cp_ebooks'),
    path('cp/qpapers', cp_qpapers, name='cp_qpapers'),
    path('cp/prac', cp_prac, name='cp_prac'),

    path('ee/', ee, name='ee'),
    path('em/', em, name='em'),
    path('ed/', ed, name='ed'),
    path('cs/', cs, name='cs'),
    path('physics/', physics, name='physics'),
    path('physicssem/', physicsstream, name='physicssem'),
    path('chemistrysem/', chemstream, name='chemistrysem')
]

