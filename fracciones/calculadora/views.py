from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from json import loads, dumps
import sqlite3

class Fraccion:
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__,sort_keys = False, indent=4)
# Create your views here.
def index(request):
    #return HttpResponse('<h1> Bienvenidos a la sesión del jueves!</h1>')
    return render(request, 'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('Hola '+ nombre)

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    r1 = int(numerador1)*int(numerador2)
    r2 = int(denominador1)*int(denominador2)
    resultado = Fraccion(r1,r2)
    json_res = resultado.toJSON()
    return HttpResponse(json_res,content_type="text/json-comment-filtered")
    #return HttpResponse("La multiplicacion de " +numerador1+ "/"+denominador1+"*" +numerador2+ "/"+denominador2+"= " + str(r1)+"/"+str(r2))

@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    r1 = (int(numerador1)*int(denominador2))+(int(numerador2)*int(denominador1))
    r2 = int(denominador1)*int(denominador2)
    resultado = Fraccion(r1,r2)
    json_res = resultado.toJSON()
    return HttpResponse(json_res,content_type="text/json-comment-filtered")
    #{"num": 2,"den": 2}
    
    #return HttpResponse("La suma de " +numerador1+ "/"+denominador1+"+" +numerador2+ "/"+denominador2+"= " + str(r1)+"/"+str(r2))

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    r1 = (int(numerador1)*int(denominador2))-(int(numerador2)*int(denominador1))
    r2 = int(denominador1)*int(denominador2)
    resultado = Fraccion(r1,r2)
    json_res = resultado.toJSON()
    return HttpResponse(json_res,content_type="text/json-comment-filtered")
    #return HttpResponse("La resta de " +numerador1+ "/"+denominador1+"-" +numerador2+ "/"+denominador2+"= " + str(r1)+"/"+str(r2))

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']
    r1 = int(numerador1)*int(denominador2)
    r2 = int(numerador2)*int(denominador1)
    resultado = Fraccion(r1,r2)
    json_res = resultado.toJSON()
    return HttpResponse(json_res,content_type="text/json-comment-filtered")
    #return HttpResponse("La division de " +numerador1+ "/"+denominador1+"/" +numerador2+ "/"+denominador2+"= " + str(r1)+"/"+str(r2))

def usuarios(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res =cur.execute("SELECT * FROM usuarios")
    resultado = res.fetchall()
  
    return render(request, 'datos.html', {'resultado':resultado})
#Entrada: {"numerador1":1,"denominador1":2,"numerador2":1,"denominador2":2}
  
#http://127.0.0.1:8000/division?numerador1=1&denominador1=4&numerador2=1&denominador2=5

@csrf_exempt
def usuarios_p(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    grado = eljson['grado']
    grupo = eljson['grupo']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)",(grupo, grado, num_lista))
    con.commit()
    return HttpResponse(grado+grupo+num_lista)

@csrf_exempt
def usuarios_d(request):
   body = request.body.decode('UTF-8')
   eljson = loads(body)
   id = eljson['id']
   con = sqlite3.connect("db.sqlite3")
   cur = con.cursor()
   res = cur.execute("DELETE FROM usuarios WHERE id_usuario=?",(str(id)))
   con.commit()
   return HttpResponse('OK usuario borrado'+str(id))