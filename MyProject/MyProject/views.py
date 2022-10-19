from pipes import Template
from django.http import HttpResponse
from django.template import Context
import datetime



#Request: Realiza peticiones
#HttpResponse: Enviar respuesta por medio de HTTP

def bienvenida(request):
    return HttpResponse("Hola mundo")

def bienvenida_rojo(request):
    return HttpResponse("<p style = 'color: red;'> Hola mundo. </p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultez"
    else:
        if edad <= 10:
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"
    resultado = "<h1>Categoria de la edad: %s </h1>" %categoria
    return HttpResponse(resultado)

def momentoActual(request):
    #respuesta = "<h1>Momento actual:{0}</h1>".format(datetime.datetime.now())
    respuesta = "<h1>Momento actual:{0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body>
    """ % (nombre,edad)
    return HttpResponse(contenido)

def plantilla(request):
    #Se abre el documento que contiene la plantilla
    plantillaExterna = open("C:/MyProject/MyProject/Plantillas/primeraPlantilla.html")
    #Se carga el documento en una variable tipo Template
    template = Template(plantillaExterna.read())
    #Se cierra el documento externo que se ha abierto
    plantillaExterna.close()
    #Se crea un contexto
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)