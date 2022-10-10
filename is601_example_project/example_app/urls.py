from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("premium/", views.premium_baked_goods, name="premium"),
]
