from django.shortcuts import render, redirect
# Create your views here.

from .forms import GirisFormu, KayitFormu
from django.contrib.auth import authenticate, login, logout

#from django.contrib.auth.models import User

def giris_view(request):
  giris_form=GirisFormu(request.POST or None)

  if giris_form.is_valid():
    kullanici_adi_viewde=giris_form.cleaned_data.get('kullanici_adi')
    sifre_viewde=giris_form.cleaned_data.get('sifre')

    uye=authenticate(username=kullanici_adi_viewde,password=sifre_viewde)

    login(request,uye)

    return redirect('ana_sayfa_URLismi')    

  return render(request,'UyeHesaplariTemplates/giris.html',{'GirisFormuAnahtar':giris_form, 'UyeIslemTurAnahtar':'Giriş'})



def kayit_view(request):
  kayit_form=KayitFormu(request.POST or None)  

  if kayit_form.is_valid():
    yeni_kullanici=kayit_form.save(commit=False)    

    sifre_viewde=kayit_form.cleaned_data.get('sifre1')

    yeni_kullanici.set_password(sifre_viewde)

    yeni_kullanici.is_staff=True
    yeni_kullanici.is_superuser=True

    yeni_kullanici.save()

    yeni_uye=authenticate(username=yeni_kullanici.username, password=sifre_viewde)

    login(request,yeni_uye)
    return redirect('ana_sayfa_URLismi')

  return render(request,'UyeHesaplariTemplates/giris.html',{'GirisFormuAnahtar':kayit_form, 'UyeIslemTurAnahtar':'Kayıt'})


def cikis_view(request):
  logout(request)
  return redirect('ana_sayfa_URLismi')
