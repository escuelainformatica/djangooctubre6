import math

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render

from login_app.modelos.Usuario import Usuario






def vista_listado(request:WSGIRequest,numpagina:int=1):

    usuarios=Usuario.objects.order_by('cuenta').all() # es una consulta en la base de datos 'select * from usuarios'
    conteo=math.ceil(Usuario.objects.count()/5.0) # numeros de paginas
    listado_conteo=range(1,conteo+1) # 1,2,3,4,5
    paginator=Paginator(usuarios,5) # creamos un objeto paginador.
    users = paginator.page(numpagina) # hacemos la paginacion
    pagprev=numpagina-1
    pagnext=numpagina+1

    context={
        'usuarios':users
        ,'listado_conteo':listado_conteo
        ,'conteo':conteo
        ,'numpagina':numpagina
        ,'pagprev':pagprev
        ,'pagnext':pagnext
    }
    return render(request,'listado.html',context)