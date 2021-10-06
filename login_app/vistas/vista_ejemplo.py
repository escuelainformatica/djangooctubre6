import json

from django.core import serializers
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from login_app.modelos.Usuario import Usuario


def vista_ejemplo(request:WSGIRequest):
    sesjson=request.session.get('usrses')
    usrs=json.loads(sesjson)
    model1=Usuario()
    model1.constructor(usrs)
    contexto={"usr":model1}
    return render(request,"interior.html",contexto)