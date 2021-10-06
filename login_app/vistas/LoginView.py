import json

from django.core import serializers
from django.core.handlers.wsgi import WSGIRequest
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
# from django.core import serializers


from login_app.modelos.Usuario import Usuario
from login_app.utilidad.Logeo import Logeo


class LoginView(View):
    def get(self,request):
        usr=Usuario()
        contexto={'usr':usr,'mensaje':''}
        return render(request,'login.html',contexto)
        # return HttpResponse("<h1>22222</h1>")

    def post(self,request:WSGIRequest):
        usr = Usuario() # usuario enviando por formulario
        try:
            usr.cuenta=request.POST['cuenta']
            usr.clave=request.POST['clave']
            # filtrado donde la cuenta y la clave sean iguales
            usr2= Usuario.objects.filter(cuenta=usr.cuenta,clave=usr.clave).first()  # 1 objeto
        except Exception as err:
            Logeo.agregarerror(f'No se pudo leer el usuario desde la base de datos {err}')
            usr2=None
        if(usr2==None):
            contexto = {'usr': usr, 'mensaje': 'usuario o clave no correcto'}
            return render(request, 'login.html', contexto)

        request.session.create()
        dic=model_to_dict(usr2)
        # valores=list(usr2.objects.all().values())
        request.session['usrses']=json.dumps(dic) # serializers.serialize('json', [dic])
        return redirect('/pagina/') # si estoy logeado

