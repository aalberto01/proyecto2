
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ast import literal_eval
import os
import json

extension = ".txt"
nombreArchivo = "archivo"
nombreIndice = "indice"
caracterdiferenciador = "|"
caractervacio = "_"
caracterEliminado = "/"
tamanioArchivo = 0


class registros(APIView):
    def get(self,request):
        archivo = open(nombreArchivo+extension, "a+")
        archivo.seek(0, 2)
        tamanioArchivo = (archivo.tell())
        archivo.seek(0, 0)
        campos = literal_eval(archivo.readline())
        caracter = ""
        registro=""
        registros=[]
        while(archivo.tell() < tamanioArchivo):
            caracter = archivo.read(1)
            while((caracter != caracterdiferenciador)):
                registro+=caracter             
                    #print(caracter, end="")
                caracter = archivo.read(1)
            registros.append(registro)
            registro=""
        archivo.close()
        return Response({'campos':campos,'registros':(registros)})
    def post(self,request):
        print("registro")
        archivo = open(nombreArchivo+extension, "r+")
        archivo.seek(0, 0)
        campos = literal_eval(archivo.readline())
        archivo.seek(0, 2)
        registro = request.data.get('registro')
        archivo.write(str(registro))
        archivo.close()
        return Response(status=status.HTTP_200_OK)
class archivo(APIView):
    def post(self,request):
        archivo = open(nombreArchivo+extension, "w")
        archivo.write(str(request.data.get('campos')))
        archivo.write("\n")
        archivo.close()
        archivo = open(nombreIndice+extension, "w")
        archivo.write(str(request.data.get('indiceHeader')))
        archivo.write("\n")
        archivo.close()

        return Response(status=status.HTTP_200_OK)
