from django.shortcuts import render, HttpResponse
# Create your views here.

def ana_sayfa_gorunumu(request):
    #return HttpResponse('<b> Burası CAppAdiAnaSayfa APP nin ana sayfası</b>')
    if request.user.is_authenticated:
        context={'isim':'zafer'}
    else:
        context={'isim':'misafir'}

    return render(request,'AnaSayfa.html',context)
