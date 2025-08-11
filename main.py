import random
import funciones
print("Bienvenido a Dia de Bosqueda","\n","seleccione la dificultad","\n","facil, 13 horas","\n","normal, 26 horas","\n","dificil, 52 horas","\n","supervivencia, hasta donde puedas")
respuesta=input()
respuesta=respuesta.lower()
while respuesta!="facil" and respuesta!="normal" and respuesta!="dificil" and respuesta!="supervivencia":
  print("")
if respuesta=="facil":
     print(" Te has perdido en el bosque, estas con poca bateria","\n","tu amigo dijo que vendrian por ti en 13 horas")
     horas=13
elif respuesta=="normal":
     print(" Te has perdido en el bosque, estas con poca bateria","\n","tu amigo dijo que vendrian por ti en 26 horas")
     horas=26
elif respuesta=="dificil":
     print(" Te has perdido en el bosque, estas con poca bateria","\n","tu amigo dijo que vendrian por ti en 52 horas")
     horas=52
elif respuesta=="supervivencia":
     print(" Te has perdido en el bosque, venias solo","\n","gritas por ayuda pero nadie viene","\n","sobrevive cuanto puedas")
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
     print(" Hora numero",horasjugadas)
     if palos>0:
      print(" Tienes",palos,"palos")
     if hojas>0:
      print(" Tienes",hojas,"hojas")
     if piedras>0:
      print(" Tienes",piedras,"piedras")
     if lianas>0:
      print(" Tienes",lianas,"lianas")
     if hojas>0:
      print(" Tienes",hojas,"hojas")
     if frutos>0:
      print(" Tienes",frutos,"frutos")
     if bengala==1:
      print(" Tienes una bengala")
     if navaja==1:
      print(" Tienes una navaja")
     if lanza==1:
      print(" Tienes una lanza")
     if hacha==1:
      print(" Tienes un hacha")
     print(" Tienes",salud,"de salud")
     print(" ¿Quiere quedarse o explorar?","\n")
     decision=input()
     decision=decision.lower()
     if decision=="quedarse":
        print(" ¿Que quieres hacer entonces?","\n"," -Hacer nada")
        if lanza==0 and palos>=2 and piedras >=1 and lianas>=2:
            print(" -Hacer lanza")
        if hacha==0 and palos>=1 and piedras >=2 and lianas>=2:
            print(" -Hacer hacha")
        if refugio==0 and palos>=10 and hojas>=20:
            print(" -Hacer un refugio")
        if fogata==0 and palos>=5 and piedras>=8:
            print(" -Hacer fogata")
        if hacha==1:
            print(" -Talar")
        if horasfogata>0:
            print(" -Alimentar fogata")
        if frutos>0:
            print(" -Comer")
        if lianas>0 and lesion>0:
            print(" -Curarse")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="hacer lanza" and lanza==0 and palos>=2 and piedras>=1 and lianas>=2:
                print(" Haz creado una lanza")
                palos=palos-2
                piedras=piedras-1
                lianas=lianas-2
                lanza==1
                usoslanza==3
        elif respuesta=="hacer hacha" and hacha==0 and palos>=1 and piedras >=2 and lianas>=2:
                print(" Haz creado un hacha")
                palos=palos-1
                piedras=piedras-2
                lianas=lianas-2
                hacha==1
                usoshacha==3
        elif respuesta=="hacer un refugio" and refugio==0 and palos>=10 and hojas>=20:
                print(" Haz construido tu refugio")
                palos=palos-10
                hojas=hojas-20
                refugio==1
        elif respuesta=="hacer fogata" and fogata==0 and palos>=5 and piedras>=8:
                print(" Haz hecho una fogata")
                palos=palos-5
                piedras=piedras-8
                fogata==1
                horasfogata==5
        elif respuesta=="talar" and hacha==1:
                print(" Haz talado el arbol")
                palosencontrados=random.randint(3,6)
                lianasencontradas=random.randint(2,4)
                hojasencontradas=random.randint(4,9)
                frutosencontrados=random.randint(1,3)
                usoshacha=usoshacha-1
                if usoshacha==0:
                    hacha=0
                    print(" ¡Oh no, se te rompio el hacha!")
                print(" Haz conseguido",frutosencontrados,"frutos,","\n",palosencontrados,"palos,","\n",hojasencontradas,"hojas y","\n",lianasencontradas,"lianas","\n")
        elif respuesta=="alimentar fogata" and horasfogata>0:
                alimentar=int(input(" ¿cuantos palos quieres poner?, escribe solo el numero"))
                horasfogata=horasfogata+alimentar
        elif respuesta=="comer" and frutos>0:
            print(" Haz comido, ahora te sientes mejor")
            frutos=frutos-1
            salud=salud+50
            while salud>saludmaxima:
                salud=salud-1
        elif respuesta=="curarse" and lianas>0 and lesion>1:
            print(" Cuantas lianas quieres usar del 1 al",lianas)
            lianascura=int(input)
            lianas=lianas-lianascura
            while lianas<0:
                lianas=lianas+1
                lianascura=lianascura-1
            aux=lianascura
            efectocura=aux*5
            lesion=lesion-lianascura
            efectolesion=efectolesion-efectocura
            while efectolesion<0:
                efectolesion=efectolesion+1
            while lesion<0:
                lesion=lesion+1
                lianas=lianas+1
            print(" Estas curado")
        else:
            print(" No podias asi que decidiste descansar")
     elif decision=="explorar":
        palosencontrados=random.randint(1,3)
        print(" Haz encontrado",palosencontrados,"palo/s")
        piedrasencontradas=random.randint(1,3)
        print(" Viste",piedrasencontradas,"piedra/s")
        lianasencontradas=random.randint(1,2)
        print(" Encontraste",lianasencontradas,"liana/s")
        frutosencontrados=random.randint(1,2)
        print(" Haz encontrado",frutosencontrados,"fruto/s")
        hojasencontradas=random.randint(2,5)
        print(" Encontraste",hojasencontradas,"hoja/s")
        palos=palos+palosencontrados
        piedras=piedras+piedrasencontradas
        lianas=lianas+lianasencontradas
        frutos=frutos+frutosencontrados
        hojas=hojas+hojasencontradas
        if palos>30:
            palos=30
        if piedras>30:
            piedras=30
        if lianas>30:
            lianas=30
        if frutos>30:
            frutos=30
        if hojas>30:
            hojas=30
        if bengala==0:
            posiblebengala=random.randint(1,20)
            if posiblebengala>16:
                print(" Felicidades, ahora tienes una bengala")
                bengala=1
        if navaja==0:
            posiblenavaja=random.randint(1,20)
            if posiblenavaja>18:
                print(" Perfecto, una navaja")
                navaja=1
                usosnavaja=7
     else:
         print(" Decidiste quedarte viendo por una hora")
     if aux%5==0:
      enemigo=random.randint(1,5)
      if enemigo==1:
        print(" Oh no, te encontraste con un oso, ¿que vas a hacer?","\n"," -Trepar","\n"," -Correr","\n")
        if navaja==1:
            print(" -Atacar con navaja","\n")
        if lanza==1:
            print(" -Atacar con lanza","\n")
        if hacha==1:
            print(" -Atacar con hacha","\n")
        if bengala==1:
            print(" -Ahuyentar","\n")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="trepar":
            print(" El oso tambien puede trepar","\n","saltas desde el arbol hacia otro y")
            resultado=random.randint(1,20)
            if resultado>10:
                print("lo logras, el oso se cansa y se va")
            else:
                if navaja==1 or hacha==1 or lanza==1:
                    print("te caiste, te lesionaste, pero todavia puedes defenderte, aleja al oso con")
                    if navaja==1:
                        print(" -Navaja")
                    if hacha==1:
                        print(" -Hacha")
                    if lanza==1:
                        print(" -Lanza")
                    if bengala==1:
                        print(" -Bengala")
                    respuesta=input()
                    respuesta=respuesta.lower()
                    if respuesta=="lanza" and lanza==1:
                        funciones.ataquelanza(lanza,usoslanza)
                    elif respuesta=="hacha" and hacha==1:
                        funciones.ataquehacha(hacha,usoshacha)
                    elif respuesta=="navaja" and navaja==1:
                        funciones.ataquenavaja(navaja,usosnavaja)
                    elif respuesta=="bengala" and bengala==1:
                        funciones.ahuyentar(bengala)
                    else:
                        funciones.dejarsemorir(salud,saludmaxima)
                    lesion=lesion+1
                    efectolesion=efectolesion+5
                else:
                    funciones.dejarsemorir(salud,saludmaxima)
        elif respuesta=="correr":
            print(" Haz huido del oso y")
            resultado=random.randint(1,20)
            if resultado==20:
                print("te tropezaste en medio de la huida")
                if navaja==1 or hacha==1 or lanza==1:
                    print("pero todavia puedes defenderte, aleja al oso con")
                    if navaja==1:
                        print(" -Navaja")
                    if hacha==1:
                        print(" -Hacha")
                    if lanza==1:
                        print(" -Lanza")
                    respuesta==input().lower()
                    if respuesta=="lanza" and lanza==1:
                        funciones.ataquelanza(lanza,usoslanza)
                    elif respuesta=="hacha" and hacha==1:
                        funciones.ataquehacha(hacha,usoshacha)
                    elif respuesta=="navaja" and navaja==1:
                        funciones.ataquenavaja(navaja,usosnavaja)
                    else:
                        funciones.dejarsemorir(salud,saludmaxima)
                else:
                    funciones.dejarsemorir(salud,saludmaxima)
        elif respuesta=="atacar con lanza":
            print(" Te pusiste su piel encima")
            funciones.ataquelanza(lanza,usoslanza)
            if saludmaxima<150:
             saludmaxima=saludmaxima+50
             salud=saludmaxima
        elif respuesta=="atacar con hacha":
            print(" Te pusiste su piel encima")
            funciones.ataquehacha(hacha,usoshacha)
            if saludmaxima<150:
             saludmaxima=saludmaxima+50
             salud=saludmaxima
        elif respuesta=="atacar con navaja":
            print(" Te pusiste su piel encima")
            funciones.ataquenavaja(navaja,usosnavaja)
            if saludmaxima<150:
             saludmaxima=saludmaxima+50
             salud=saludmaxima
        elif respuesta=="ahuyentar":
            funciones.ahuyentar(bengala)
        else:
            funciones.dejarsemorir(salud,saludmaxima)
      elif enemigo==2:
        print(" Ves a otro humano, pero este te empieza a atacar","\n","es un cazador, pero no esta bien de la cabeza","\n"," ¿Que vas a hacer?")
        print(" -Huir","\n"," -Esconderte")
        if bengala==1:
            print(" -Ahuyentarlo")
        if lanza==1:
            print(" -Arrojar lanza")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="huir":
            suerte=random.randint
            if suerte>10:
                print(" Trataste de escapar, pero el cazador te pego un disparo a la cabeza")
                salud=salud-salud
            else:
                print(" Escapaste con exito")
        elif respuesta=="esconderse":
            print(" Te has escondido detras de un arbol","\n","el cazador avanza buscandote","\n"," ¿Que haras ahora?")
            print(" -Huir lentamente")
            if hacha==1:
                print(" -Usar hacha")
            if navaja==1:
                print(" -Usar navaja")
            respuesta==input()
            respuesta=respuesta.lower()
            if respuesta=="usar hacha":
                funciones.ataquehacha(hacha,usoshacha)
            elif respuesta=="usar navaja":
                funciones.ataquenavaja(navaja,usosnavaja)
            else:
                print(" haz escapado de la situacion con exito")
        elif respuesta=="arrojar lanza":
            funciones.ataquelanza(lanza,usoslanza)
        elif respuesta=="ahuyentarlo":
            funciones.ahuyentar(bengala)
        else:
            funciones.dejarsemorir(salud,saludmaxima)
      elif enemigo==3:
        print(" Oh no, el arbol cobro vida","\n"," ¿Que vas a hacer?","\n"," -Forcejear")
        if hacha==1:
            print(" -Talar","\n")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="forcejear":
            suerte=random.randint(1,20)
            if suerte>=14:
                print(" Haz logrado huir con exito","\n")
            else:
                print(" Haz escapado, pero te has lesionado una pierna en el proceso","\n")
                lesion=lesion+1
                efectolesion=efectolesion+5
        elif respuesta=="talar" and hacha==1:
            funciones.ataquehacha(hacha,usoshacha)
        else:
            print(" Dejaste que el arbol hiciera lo que quisiera contigo","\n")
            lesion=lesion+1
            efectolesion==efectolesion+5
      elif enemigo==4:
        print(" Sientes un aullido a lo lejos","\n","es un lobo enorme","\n", " ¿Que vas a hacer?","\n"," -Intimidarlo","\n"," -Alejarte")
        if bengala==1:
            print(" -Ahuyentarlo")
        if lanza==1:
            print(" -Atacar con lanza")
        if hacha==1:
            print(" -Atacar con hacha")
        if navaja==1:
            print(" -Atacar con navaja")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="intimidarlo":
            print(" Haz intentado ahuyentarlo y")
            suerte=random.randint(1,20)
            if suerte>=14:
                print(" El lobo se fue sin atacar")
            else:
                print(" El lobo se enojo aun mas","\n","¿como saldras de esta?")
                if bengala==1:
                 print(" -Ahuyentarlo")
                if lanza==1:
                 print(" -Atacar con lanza")
                if hacha==1:
                 print(" -Atacar con hacha")
                if navaja==1:
                 print(" -Atacar con navaja")
                respuesta=input()
                respuesta=respuesta.lower()
                if respuesta=="ahuyentarlo" and bengala==1:
                    funciones.ahuyentar(bengala)
                elif respuesta=="atacar con lanza" and lanza==1:
                    funciones.ataquelanza(lanza,usoslanza)
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                elif respuesta=="atacar con hacha" and hacha==1:
                    funciones.ataquehacha(hacha,usoshacha)
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                elif respuesta=="atacar con navaja" and navaja==1:
                    print(" Usaste su piel para el frio")
                    funciones.ataquelanza(lanza,usoslanza)
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                else:
                    funciones.dejarsemorir(salud,saludmaxima)
        elif respuesta=="alejarte":
            print("Haz intetado escapar, pero el lobo te salto encima","\n"," ¿Que haras al respecto?")
            if bengala==1:
                 print(" -Ahuyentarlo")
            if lanza==1:
                 print(" -Atacar con lanza")
            if hacha==1:
                 print(" -Atacar con hacha")
            if navaja==1:
                 print(" -Atacar con navaja")
            respuesta=input()
            respuesta=respuesta.lower()
            if respuesta=="ahuyentarlo" and bengala==1:
                funciones.ahuyentar(bengala)
            elif respuesta=="atacar con lanza" and lanza==1:
                funciones.ataquelanza(lanza,usoslanza)
                if saludmaxima!=130 or saludmaxima!=180:
                    saludmaxima=saludmaxima+30
            elif respuesta=="atacar con hacha" and hacha==1:
                funciones.ataquehacha(hacha,usoshacha)
                if saludmaxima!=130 or saludmaxima!=180:
                    saludmaxima=saludmaxima+30
            elif respuesta=="atacar con navaja" and navaja==1:
                print(" Usaste su piel para el frio")
                funciones.ataquelanza(lanza,usoslanza)
                if saludmaxima!=130 or saludmaxima!=180:
                    saludmaxima=saludmaxima+30
            else:
                funciones.dejarsemorir(salud,saludmaxima)
        elif respuesta=="ahuyentarlo" and bengala==1:
                funciones.ahuyentar(bengala)
        elif respuesta=="atacar con lanza" and lanza==1:
            funciones.ataquelanza(lanza,usoslanza)
            if saludmaxima!=130 or saludmaxima!=180:
                saludmaxima=saludmaxima+30
        elif respuesta=="atacar con hacha" and hacha==1:
            funciones.ataquehacha(hacha,usoshacha)
            if saludmaxima!=130 or saludmaxima!=180:
                saludmaxima=saludmaxima+30
        elif respuesta=="atacar con navaja" and navaja==1:
            print(" Usaste su piel para el frio")
            funciones.ataquelanza(lanza,usoslanza)
            if saludmaxima!=130 or saludmaxima!=180:
                saludmaxima=saludmaxima+30
        else:
            funciones.dejarsemorir(salud,saludmaxima)
      elif enemigo==5 and horasjugadas>=20:
        print(" Una ola de frio ha aparecido")
        if fogata==1:
            print(" Te quedaste alimentando a tu fogata para que se mantenga viva un poco mas","\n","lograste que sobreviva, pero igual se redujo mucho")
            horasfogata=horasfogata-2
            if horasfogata<=0:
                print(" La fogata se ha apagado")
                fogata=0
                horasfogata=0
            palos=palos-5
            if palos<0:
                palos=0
        else:
            funciones.dejarsemorir(salud,saludmaxima)
      else:
        print(" Creiste que habia pasado algo raro, pero nada mas alejado de la verdad")
     if horasjugadas>100:
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
    print(" Felicidades, te rescataron, ahora eres libre de ese bosque")
elif salud<=0:
    print(" Usted ha muerto")
else:
    print(" A duras penas llegaste al final, los rescatistas te salvaron de la muerte por milesimas")

