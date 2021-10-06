from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from login_app.vistas.LoginView import LoginView  # LoginView()
from login_app.vistas.vista_listado import vista_listado
from login_app.vistas.vista_ejemplo import vista_ejemplo  # import vistas.LoginView


# import vistas.vista_ejemplo # vistas.LoginView.LoginView()
# Create your views here.

def vista_upload(request: WSGIRequest):
    if (request.method == 'POST'):
        resultado = handle_uploaded_file(request.FILES['file'])
        if resultado == False:
            archivo = None
        else:
            archivo = request.FILES['file'].name
    else:
        archivo = None

    contexto = {"archivo": archivo}
    return render(request, "upload.html", contexto)


# c:\carpeta  <-- windows errores.
# c:/carpeta

def handle_uploaded_file(f):
    if (f.content_type != 'image/png'):
        return False
    try:
        with open('C:/cursopython/djangoProject8/login_app/static/' + f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except:
        pass
    return True
