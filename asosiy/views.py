from django.shortcuts import render, redirect
from .models import *
from .forms import *


def studentlar(request):
    data = {
        "students" : Student.objects.all()
    }
    return render(request, 'studentlar.html', data)

def rejalar(request):
    if request.method == "POST":
        form = RejaForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/rejalar/")
    data = {
        "rejalar" : Reja.objects.all(),
        "form" : RejaForm
    }
    return render(request, 'rejalar.html', data)

def BitiruvchilarRejalari(request):
    data = {
        "b_rejalari": Reja.objects.filter(student__kurs=4),

    }
    return render(request, 'rejalar.html', data)

def bitta_talaba_rejasi(request, son):
    data ={
        "b_t_rejalari" : Reja.objects.filter(student__id=son)
    }
    return render(request, 'b_t_rejalari.html', data)


def bajarilmagan_rejalar(request):
    data = {
        "b_rejalar" : Reja.objects.filter( bajarilgan=False)
    }
    return render(request, 'bajarilmagan_rejalar.html', data)

def u_kurslar(request):
    data = {
        "k_u_kurslar" : Student.objects.filter(kurs__gt=2)
    }
    return render(request, 'k_u_kurslar.html', data)

def reja_ochir(request, son):
    Reja.objects.get(id=son).delete()
    return redirect("/rejalar/")

