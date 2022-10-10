from django.shortcuts import render
from django.http import HttpResponse
from .models import BakedGood


def index(request):
    baked_goods = BakedGood.objects.all()
    context = {"baked_goods": baked_goods}
    return render(request, "example_app/for.html", context)


def premium_baked_goods(request):
    baked_goods = BakedGood.objects.all()
    context = {"baked_goods": baked_goods}
    return render(request, "example_app/premium.html", context)
