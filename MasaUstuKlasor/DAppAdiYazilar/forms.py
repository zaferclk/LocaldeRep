from django import forms
from .models import YazilarTabloAdiKlasi, YorumlarTabloAdiKlasi
from captcha.fields import ReCaptchaField

class YazilarFormu(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model=YazilarTabloAdiKlasi
        fields=[
            'baslik',
            'metin',
            'yuklenen_dosya',            
        ]

class YorumlarFormu(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model=YorumlarTabloAdiKlasi
        fields=[
            'yorum_yapanin_adi',
            'yorum_metni',       
        ]