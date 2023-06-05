from django.shortcuts import render, redirect
from .models import *
from userapp.models import Ombor
from django.views import View
from statsapp.models import Statistika

def client(request):
    if request.user.is_authenticated:
        content = {
            "mijoz": Mijoz.objects.filter(ombor1 = Ombor.objects.get(user = request.user))
        }
        return render(request, 'clients.html', content)
    return redirect('/')

def bolimlar(request):
    if request.user.is_authenticated:
        return render(request, 'bulimlar.html')
    return redirect('/')

def client_update(request):
    return render(request, 'client_update.html')

def product_update(request):
    return render(request, 'product_update.html')

def products(request):
    if request.method == 'POST':
        Mahsulot.objects.create(ombor1 = Ombor.objects.get(user = request.user),
            nom = request.POST['nom'],
            brend = request.POST['brend'],
            narx = request.POST['narx'],
            miqdor = request.POST['miqdor'],
            olchov = request.POST['olchov'],
            sana = request.POST['sana'],
            )
        return redirect('/product/')
    if request.user.is_authenticated:
        content = {
            'mahsulot': Mahsulot.objects.filter(ombor1 = Ombor.objects.get(user = request.user))
        }
        return render(request, 'products.html', content)
    return redirect('/')

class MahsulotOchirView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            Mahsulot.objects.filter(id=pk, ombor1__user=request.user).delete()
            return redirect('/product/')
        return redirect('/')

class MahsulotEditView(View):
    def post(self, request, pk):
        # if request.user.is_authenticated:
            Mahsulot.objects.filter(id=pk, ombor1__user=request.user).update(
                nom = request.POST['nom'],
                brend = request.POST['brend'],
                narx = request.POST['narx'],
                miqdor = request.POST['miqdor'],
            )
            return redirect('/product/')
    def get(self, request, pk):
        content = {
            'mahsulot':Mahsulot.objects.get(id=pk)
        }
        return render(request, 'product_update.html', content)
class MijozDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            Mijoz.objects.get(id=pk, ombor1__user=request.user).delete()
            return redirect('/client/')
        return redirect('/')
class MijozEditView(View):
    def get(self, request, pk):
        content = {
            'mijoz': Mijoz.objects.get(id=pk)
        }
        return render(request, 'client_update.html', content)

    def post(self, request, pk):
        Mijoz.objects.filter(id=pk, ombor1__user=request.user).update(
            ism = request.POST['ism'],
            nom = request.POST['nom'],
            tel = request.POST['tel'],
            manzil = request.POST['manzil'],
            qarz = request.POST['qarz']
        )
        return redirect('/client/')

def stats(request):
    if request.user.is_authenticated:
        content = {
            'statistika':Statistika.objects.all(),

        }
        return render(request, 'stats.html', content)
    return redirect('/')
# Create your views here.
