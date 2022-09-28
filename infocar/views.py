import requests
from django.http import HttpResponseRedirect
from .models import Auto,Transmission,Engine
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    t = Transmission.objects.all()
    all_car = Auto.objects.all()
    return render(request, 'infocar/index.html', {'all_car': all_car,'t':t})

def create_auto(request):
    e = Engine.objects.all()
    t = Transmission.objects.all()
    if request.method == 'POST':
        r = request.POST
        try:
            Auto.objects.create(
                firm=r['firm'],
                model=r['model'],
                color=r['color'],
                volume=r['volume'],
                price=r['price'],
                engine_id=r['engine'],
                transmission_id = r['transmission']
            )
            return HttpResponseRedirect('/')
        except:
            redirect('/infocar/create.html')
    return render(request,'infocar/create.html',{'e':e,'t':t})

def edit_auto(request,id):
    e = Engine.objects.all()
    t = Transmission.objects.all()
    ed_auto = Auto.objects.get(id=id)

    if request.method == 'POST':
        r = request.POST
        print(r)
        try:
            Auto.objects.filter(id=id).update(
                firm=r['firm'],
                model=r['model'],
                color=r['color'],
                volume=float(r['volume'].replace(',','.')),
                price=r['price'],
                engine_id=r['engine'],
                transmission_id = r['transmission']
            )
            return HttpResponseRedirect('/')
        except:
            redirect('/infocar/edit.html')
        redirect('/infocar/index.html')
    return render(request,'infocar/edit.html',{'e':e,'t':t,'ed_auto':ed_auto})

def delete_auto(request,id):

    if request.method == 'POST':
        del_auto = Auto.objects.filter(id=id)
        del_auto.delete()

        return HttpResponseRedirect('/')
def get_mechanical (request,id):
    trans = Transmission.objects.get(id=id)
    res = trans.auto_set.all()
    t = Transmission.objects.all()
    return render(request,'infocar/transmission.html',{'res':res,'t':t})
