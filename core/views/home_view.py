from django.shortcuts import render


def home_core(request, template_name="home.html"):
    nome = "Gabriel"
    return render(request, template_name, {'nome': nome})