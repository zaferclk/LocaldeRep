from django.urls import path, re_path
from .views import *

app_name='yazi_app_name'

urlpatterns=[
    path('',ana_sayfa_index_view),
    path('index/',ana_sayfa_index_view,name='index_URLismi'),

    path('olustur/',ana_sayfa_olustur_view, name='olustur_URLismi'),

    #re_path(r'^(?P<slug>[\w-]+)/$',ana_sayfa_ayrinti_view, name='ayrinti_URLismi'),
    re_path(r'^(?P<id>\d+)/$',ana_sayfa_ayrinti_view, name='ayrinti_URLismi'),

    
    #re_path(r'^(?P<slug>[\w-]+)/guncelle/$',ana_sayfa_guncelle_view, name='guncelle_URLismi'),
    re_path(r'^(?P<id>\d+)/guncelle/$',ana_sayfa_guncelle_view, name='guncelle_URLismi'),

    
    #re_path(r'^(?P<slug>[\w-]+)/sil/$',ana_sayfa_sil_view, name='sil_URLismi'),
    re_path(r'^(?P<id>\d+)/sil/$',ana_sayfa_sil_view, name='sil_URLismi'),
]