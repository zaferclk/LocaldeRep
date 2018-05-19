from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
# Create your views here.
from .models import YazilarTabloAdiKlasi
from .forms import YazilarFormu, YorumlarFormu
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator

from django.db.models import Q

def ana_sayfa_index_view(request):
    tum_yazilar=YazilarTabloAdiKlasi.objects.all()

    sorgu=request.GET.get('q')
    if sorgu:
        tum_yazilar=tum_yazilar.filter( 
            Q(baslik__icontains=sorgu) | 
            Q(metin__icontains=sorgu) | 
            Q(yazar_modelden__first_name__icontains=sorgu) | 
            Q(yazar_modelden__last_name__icontains=sorgu) 
        ).distinct()

    sayfalama = Paginator(tum_yazilar,5)

    URL_deki_sayfa_no = request.GET.get('sayfa')
    her_sayfadaki_yazilar = sayfalama.get_page(URL_deki_sayfa_no)

    return render(request,'YazilarTemplates/index.html',{'TumYazilarAnahtar':her_sayfadaki_yazilar})    

    #return render(request,'YazilarTemplates/index.html',{'TumYazilarAnahtar':tum_yazilar})
    
    #return HttpResponse('<b>DAppAdiYazilar ın index sayfası</b>')

def ana_sayfa_ayrinti_view(request, id):
    #tek_bir_yazi=YazilarTabloAdiKlasi.objects.get(id=1)
    #return render(request,'YazilarTemplates/ayrinti.html',{'TekBirYaziAnahtar':tek_bir_yazi})
    
    tek_bir_yazi=get_object_or_404(YazilarTabloAdiKlasi,id=id)

    YorumFormu=YorumlarFormu(request.POST or None)
    if YorumFormu.is_valid():
        geri_donen_yorum=YorumFormu.save(commit=False)
        geri_donen_yorum.yorum_yapilan_yazi=tek_bir_yazi
        geri_donen_yorum.save()
        return HttpResponseRedirect(tek_bir_yazi.get_absolute_url()) 

    context={'TekBirYaziAnahtar':tek_bir_yazi, 'YorumFormuAnahtar':YorumFormu}

    return render(request,'YazilarTemplates/ayrinti.html',context)
    
    #return HttpResponse('<b>DAppAdiYazilar ın AYRINTI sayfası</b>')

def ana_sayfa_olustur_view(request):

    #if not request.user.is_authenticated:
        #raise Http404()

    #OlusturFormu=YazilarFormu()
    #context={'OlusturFormuAnahtar':OlusturFormu,}


    #if request.method=="POST":
        #print(request.POST)
    
        #baslik_formdan_gelen=request.POST.get('baslik')
        #metin_formdan_gelen=request.POST.get('metin')
        #YazilarTabloAdiKlasi.objects.create(baslik=baslik_formdan_gelen, metin=metin_formdan_gelen)
    

    #if request.method=="POST":
        #OlusturFormu=YazilarFormu(request.POST)
        #if OlusturFormu.is_valid():
            #OlusturFormu.save()
    #else:
        #OlusturFormu=YazilarFormu()
        

    OlusturFormu=YazilarFormu(request.POST or None, request.FILES or None )
    if OlusturFormu.is_valid():
        geri_donen_yazi=OlusturFormu.save(commit=False)
        geri_donen_yazi.yazar_modelden=request.user
        geri_donen_yazi.save()
        messages.success(request,'görülmesini istediğimiz mesaj',extra_tags='bizim-class')

        #geri_donen_yazi=OlusturFormu.save(commit=False)
        #geri_donen_yazi.slug_alani_modelden=slugify(geri_donen_yazi.baslik.replace('ı','i'))
        #geri_donen_yazi.save()

        return HttpResponseRedirect(geri_donen_yazi.get_absolute_url())      

    context={'OlusturFormuAnahtar':OlusturFormu,}

    return render(request,'YazilarTemplates/olustur.html',context)

    #return HttpResponse('<b>DAppAdiYazilar ın OLUŞTUR sayfası</b>')

#def ana_sayfa_guncelle_view(request,id):
def ana_sayfa_guncelle_view(request,id):

    #if not request.user.is_authenticated:
        #raise Http404()

    #tek_bir_yazi=get_object_or_404(YazilarTabloAdiKlasi,id=id)
    tek_bir_yazi=get_object_or_404(YazilarTabloAdiKlasi,id=id)
    GuncelleFormu=YazilarFormu(request.POST or None,request.FILES or None, instance=tek_bir_yazi)

    if GuncelleFormu.is_valid():
        GuncelleFormu.save()
        messages.success(request,'görülecek mesaj metni - güncelleme',extra_tags='bizim_class')
        return HttpResponseRedirect(tek_bir_yazi.get_absolute_url())  

    context={'OlusturFormuAnahtar':GuncelleFormu,}

    return render(request,'YazilarTemplates/olustur.html',context)

    #return HttpResponse('<b>DAppAdiYazilar ın GÜNCELLE sayfası</b>')

def ana_sayfa_sil_view(request,id):

    #if not request.user.is_authenticated:
        #raise Http404()

    tek_bir_yazi=get_object_or_404(YazilarTabloAdiKlasi,id=id)
    
    tek_bir_yazi.delete()

    return redirect('yazi_app_name:index_URLismi')

    #return HttpResponse('<b>DAppAdiYazilar ın SİL sayfası</b>')
