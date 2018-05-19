from django import forms

from django.contrib.auth import authenticate
#from captcha.fields import ReCaptchaField

from django.contrib.auth.models import User


class GirisFormu(forms.Form):
    kullanici_adi=forms.CharField(max_length=100,label='Kullanıcı Adı')
    sifre=forms.CharField(max_length=100,label='Şifre',widget=forms.PasswordInput)

    #captcha = ReCaptchaField()
    
    def clean(self):
        kullanici_adi_clean=self.cleaned_data.get('kullanici_adi')
        sifre_clean=self.cleaned_data.get('sifre')

        if kullanici_adi_clean and sifre_clean:
            uye_clean=authenticate(username=kullanici_adi_clean,password=sifre_clean)

            if not uye_clean:
                raise forms.ValidationError('yanlış giriş mesajı')
        
        return super(GirisFormu,self).clean()



class KayitFormu(forms.ModelForm):
    username=forms.CharField(max_length=100,label='Kullanıcı Adı Bizim')
    sifre1=forms.CharField(max_length=100,label='Şifre',widget=forms.PasswordInput)
    sifre2=forms.CharField(max_length=100,label='Şifre Doğrulama',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=[
            'username',
            'sifre1',
            'sifre2',
        ]    

    def clean_sifre2(self):
        sifre1_clean=self.cleaned_data.get('sifre1')
        sifre2_clean=self.cleaned_data.get('sifre2')

        if sifre1_clean and sifre2_clean and sifre1_clean != sifre2_clean:
            raise forms.ValidationError('şifreler eşleşmiyor')
        
        return sifre1_clean