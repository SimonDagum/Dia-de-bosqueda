import random
import funciones
print("Bienvenido a Dia de Bosqueda","\n","seleccione la dificultad","\n","facil, 13 horas","\n","normal, 26 horas","\n","dificil, 52 horas","\n","supervivencia, hasta donde puedas")
respuesta=input()
respuesta=respuesta.lower()
while respuesta!="facil" and respuesta!="normal" and respuesta!="dificil" and respuesta!="supervivencia":
  print("")
if respuesta=="facil":
     print("te has perdido en el bosque, estas con poca bateria","\n","tu amigo dijo que vendrian por ti en 13 horas")
     horas=13
elif respuesta=="normal":
     print("te has perdido en el bosque, estas con poca bateria","\n","tu amigo dijo que vendrian por ti en 26 horas")
     horas=26
elif respuesta=="dificil":
     print("te has perdido en el bosque, estas con poca bateria","\n","tu amigo dijo que vendrian por ti en 52 horas")
     horas=52
elif respuesta=="supervivencia":
     print("te has perdido en el bosque, venias solo","\n","gritas por ayuda pero nadie viene","\n","sobrevive cuanto puedas")
     horas=0
horasjugadas=1
piedras=0
palos=0
lianas=0
navaja=0
usosnavaja=0
bengala=0
frutos=0
hojas=0
salud=100
saludmaxima=100
lanza=0
usoslanza=0
hacha=0
usoshacha=0
fogata=0
horasfogata=0
refugio=0
lesion=0
efectolesion=0
aux=0
suerte=0
while horasjugadas!=horas and salud>0:
     aux=horasjugadas
     print("hora numero",horasjugadas,"\n")
     if palos>0:
      print("tienes",palos,"palos","\n")
     if hojas>0:
      print("tienes",hojas,"hojas")
     if piedras>0:
      print("tienes",piedras,"piedras","\n")
     if lianas>0:
      print("tienes",lianas,"lianas","\n")
     if hojas>0:
      print("tienes",hojas,"hojas","\n")
     if frutos>0:
      print("tienes",frutos,"frutos","\n")
     if bengala==1:
      print("tienes una bengala","\n")
     if navaja==1:
      print("tienes una navaja","\n")
     if lanza==1:
      print("tienes una lanza","\n")
     if hacha==1:
      print("tienes un hacha","\n")
     print("tienes",salud,"de salud","\n")
     funciones.eventocomun(palos,piedras,navaja,bengala,lianas,frutos,hojas,lanza,hacha,fogata,refugio,horasfogata,usoslanza,usoshacha,usosnavaja,salud,saludmaxima)
     if aux%5==0:
      funciones.desafio(salud,saludmaxima,lanza,usoslanza,hacha,usoshacha,fogata,horasfogata,bengala,navaja,usosnavaja,lesion,efectolesion)
     if horasjugadas>55:
      suerte=random.randint(1,1000)
      if suerte==1:
        salud=0
        print("oh no, que desgracia, los aliens llegaron y mataron a todos, sobreviviste",horasjugadas,"hora/s","\n")
     if fogata>0:
      horasfogata=horasfogata-1
      if lesion>0:
       efectolesion=efectolesion-1
       salud=salud-10
      if efectolesion==0:
       print("estas curado","\n")
       lesion=0
     salud=salud-10
     horasjugadas=horasjugadas+1
if horasjugadas==horas:
    print("felicidades, te rescataron, ahora eres libre de ese bosque","\n")
if salud<=0:
    print("haz muerto")