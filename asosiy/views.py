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

# def bitta_talaba(request, son):
#     if request.GET.get(son):
