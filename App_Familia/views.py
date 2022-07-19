from django.http import HttpResponse
from django.shortcuts import render

from App_Familia.models import Familia

# Create your views here.
def familia(self, nombre, edad, fecha_nacimiento, parentezco):
    familia = Familia(nombre = nombre, edad = edad, fecha_nacimiento = fecha_nacimiento, parentezco = parentezco)
    familia.save()
    return HttpResponse(f"""
    <p>Nombre: {familia.nombre} - Edad: {familia.edad} - Fecha Nacimiento: {familia.fecha_nacimiento} - Parentezco: {familia.parentezco} </p> """)


def lista_familiares(self):
    lista = Familia.objects.all()
    return render(self, "lista_familiares.html", {"lista_familiares": lista})