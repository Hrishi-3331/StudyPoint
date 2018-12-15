from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage),


    # Chemistry
    path('chemistry/', chem, name='chem'),
    path('chemistry/assignments', chem_ass, name='chem_assignments'),
    path('chemistry/notes', chem_notes, name='chem_notes'),
    path('chemistry/ebooks', chem_ebooks, name='chem_ebooks'),
    path('chemistry/qpapers', chem_qpapers, name='chem_qpapers'),
    path('chemistry/prac', chem_prac, name='chem_prac'),

    # Maths
    path('maths/', maths, name='maths'),
    path('maths/assignments', maths_ass, name='maths_assignments'),
    path('maths/notes', maths_notes, name='maths_notes'),
    path('maths/ebooks', maths_ebooks, name='maths_ebooks'),
    path('maths/qpapers', maths_qpapers, name='maths_qpapers'),
    path('maths/prac', maths_prac, name='maths_prac'),

    # Social Science
    path('ss/', ss, name='ss'),
    path('ss/assignments', ss_ass, name='ss_assignments'),
    path('ss/notes', ss_notes, name='ss_notes'),
    path('ss/ebooks', ss_ebooks, name='ss_ebooks'),
    path('ss/qpapers', ss_qpapers, name='ss_qpapers'),
    path('ss/prac', ss_prac, name='ss_prac'),

    # CP
    path('cp/', cp, name='cp'),
    path('cp/assignments', cp_ass, name='cp_assignments'),
    path('cp/notes', cp_notes, name='cp_notes'),
    path('cp/ebooks', cp_ebooks, name='cp_ebooks'),
    path('cp/qpapers', cp_qpapers, name='cp_qpapers'),
    path('cp/prac', cp_prac, name='cp_prac'),

    # Electrical Engineering
    path('ee/', ee, name='ee'),
    path('ee/assignments', ee_ass, name='ee_assignments'),
    path('ee/notes', ee_notes, name='ee_notes'),
    path('ee/ebooks', ee_ebooks, name='ee_ebooks'),
    path('ee/qpapers', ee_qpapers, name='ee_qpapers'),
    path('ee/prac', ee_prac, name='ee_prac'),

    # Engineering Mechanics
    path('em/', em, name='em'),
    path('em/assignments', em_ass, name='em_assignments'),
    path('em/notes', em_notes, name='em_notes'),
    path('em/ebooks', em_ebooks, name='em_ebooks'),
    path('em/qpapers', em_qpapers, name='em_qpapers'),
    path('em/prac', em_prac, name='em_prac'),

    # Engineering Drawing
    path('ed/', ed, name='ed'),
    path('ed/assignments', ed_ass, name='ed_assignments'),
    path('ed/notes', ed_notes, name='ed_notes'),
    path('ed/ebooks', ed_ebooks, name='ed_ebooks'),
    path('ed/qpapers', ed_qpapers, name='ed_qpapers'),
    path('ed/prac', ed_prac, name='ed_prac'),

    # Communication Skills
    path('cs/', cs, name='cs'),
    path('cs/assignments', cs_ass, name='cs_assignments'),
    path('cs/notes', cs_notes, name='cs_notes'),
    path('cs/ebooks', cs_ebooks, name='cs_ebooks'),
    path('cs/qpapers', cs_qpapers, name='cs_qpapers'),
    path('cs/prac', cs_prac, name='cs_prac'),

    # Physics
    path('physics/', physics, name='physics'),
    path('physics/assignments', physics_ass, name='physics_assignments'),
    path('physics/notes', physics_notes, name='physics_notes'),
    path('physics/ebooks', physics_ebooks, name='physics_ebooks'),
    path('physics/qpapers', physics_qpapers, name='physics_qpapers'),
    path('physics/prac', physics_prac, name='physics_prac'),

    # Semester Pages
    path('physicssem/', physicsstream, name='physicssem'),
    path('chemistrysem/', chemstream, name='chemistrysem')
]

