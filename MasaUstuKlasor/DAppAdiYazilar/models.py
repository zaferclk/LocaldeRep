from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class YazilarTabloAdiKlasi(models.Model):
    yazar_modelden=models.ForeignKey('auth.User',verbose_name='Yazar',on_delete=models.CASCADE,related_name='Yazilar')
    baslik=models.CharField(max_length=120, verbose_name='Başlık')
    #metin=models.TextField(verbose_name='İçerik')
    metin=RichTextField(verbose_name='İçerik')
    yayinlanma_tarihi=models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True)    
    yuklenen_dosya=models.FileField(null=True, blank=True)    
    slug_alani_modelden=models.SlugField(unique=True, editable=False, max_length=130)

    #yuklenen_dosya=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.baslik
    
    def get_absolute_url(self):
        # return "/DAppAdiYazilar/{}".format(self.id)
        return reverse('yazi_app_name:ayrinti_URLismi', kwargs = { 'id' : self.id })


    def benzersiz_slug_gonderen(self):
        hazirlanan_slug=slugify(self.baslik.replace('ı','i'))
        benzersiz_slug=hazirlanan_slug
        sayi=1
        while YazilarTabloAdiKlasi.objects.filter(slug_alani_modelden=benzersiz_slug).exists():
            benzersiz_slug='{}- {}'.format(hazirlanan_slug,sayi)
            sayi +=1
        
        return benzersiz_slug

    
    def save(self,*args,**kwargs):
        #if not self.slug_alani_modelden:
            #self.slug_alani_modelden=slugify(self.baslik.replace('ı','i'))        
        self.slug_alani_modelden=self.benzersiz_slug_gonderen()
        
        return super(YazilarTabloAdiKlasi,self).save(*args,**kwargs)

    
    class Meta:
        ordering=['-yayinlanma_tarihi','id']

class YorumlarTabloAdiKlasi(models.Model):
    yorum_yapilan_yazi=models.ForeignKey('DAppAdiYazilar.YazilarTabloAdiKlasi', related_name='Yorumlar', on_delete=models.CASCADE)
    yorum_yapanin_adi=models.CharField(max_length=200, verbose_name='Yorum Yapan')
    yorum_metni=models.TextField(verbose_name='Yorum')
    yorum_olusturulma_tarihi=models.DateTimeField(auto_now_add=True)

