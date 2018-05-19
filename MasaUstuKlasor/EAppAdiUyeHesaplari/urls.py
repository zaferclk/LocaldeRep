from django.urls import path, re_path
from .views import *

app_name='uye_app_name'

urlpatterns=[
    path('giris/',giris_view,name='uye_giris_URLismi'),
    path('kayit/',kayit_view,name='uye_kayit_URLismi'),
    path('cikis/',cikis_view,name='uye_cikis_URLismi'),  
]