from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from missoes.forms import MissaoForm
from missoes.models import Missao
from missoes.forms import NovaMissaoForm

def home(request):
    if request.method == 'POST':
        form = NovaMissaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('missoes:home'))
        else:
            missoes_pendentes = Missao.objects.filter(feita=False).all()
            missoes_feitas = Missao.objects.filter(feita=True).all()
            return render(
                request,'missoes/home.html', 
                {
                    'form':form, 
                    'missoes_pendentes': missoes_pendentes,
                    'missoes_feitas': missoes_feitas,
                },
                 status=400)
    missoes_pendentes = Missao.objects.filter(feita=False).all()  
    missoes_feitas = Missao.objects.filter(feita=True).all()      
    return render (request, 'missoes/home.html',  
                    {
                        'missoes_pendentes': missoes_pendentes,
                        'missoes_feitas': missoes_feitas,
                    })

def detalhe (request, missao_id):
    missao = Missao.objects.get(id=missao_id)
    form = MissaoForm(request.POST, instance=missao)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('missoes:home'))
