import random
def eventocomun(palos,piedras,navaja,bengala,lianas,frutos,hojas,lanza,hacha,fogata,refugio,horasfogata,usoslanza,usoshacha,usosnavaja,salud,saludmaxima,lesion,efectolesion):
    palosencontrados=0
    frutosencontrados=0
    piedrasencontradas=0
    hojasencontradas=0
    posiblebengala=0
    posiblenavaja=0
    print("¿quiere quedarse o explorar?","\n")
    decision=input()
    decision=decision.lower()
    if decision=="quedarse":
        print("¿que quieres hacer entonces?","\n")
        if lanza==0 and palos>=2 and piedras >=1 and lianas>=2:
            print("hacer lanza","\n")
        if hacha==0 and palos>=1 and piedras >=2 and lianas>=2:
            print("hacer hacha","\n")
        if refugio==0 and palos>=10 and hojas>=20:
            print("hacer un refugio","\n")
        if fogata==0 and palos>=5 and piedras>=8:
            print("hacer fogata","\n")
        if hacha==1:
            print("talar","\n")
        if horasfogata>0:
            print("alimentar fogata","\n")
        if frutos>0:
            print("comer","\n")
        if lianas>0 and lesion>0:
            print("curarse","\n")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="hacer lanza" and lanza==0 and palos>=2 and piedras>=1 and lianas>=2:
                print("haz creado una lanza","\n")
                palos=palos-2
                piedras=piedras-1
                lianas=lianas-2
                lanza==1
                usoslanza==3
        elif respuesta=="hacer hacha" and hacha==0 and palos>=1 and piedras >=2 and lianas>=2:
                print("haz creado un hacha","\n")
                palos=palos-1
                piedras=piedras-2
                lianas=lianas-2
                hacha==1
                usoshacha==3
        elif respuesta=="hacer un refugio" and refugio==0 and palos>=10 and hojas>=20:
                print("haz construido tu refugio","\n")
                palos=palos-10
                hojas=hojas-20
                refugio==1
        elif respuesta=="hacer fogata" and fogata==0 and palos>=5 and piedras>=8:
                print("haz hecho una fogata","\n")
                palos=palos-5
                piedras=piedras-8
                fogata==1
                horasfogata==5
        elif respuesta=="talar" and hacha==1:
                print("haz talado el arbol")
                palosencontrados=random.randint(3,6)
                lianasencontradas=random.randint(2,4)
                hojasencontradas=random.randint(4,9)
                frutosencontrados=random.randint(1,3)
                usoshacha=usoshacha-1
                if usoshacha==0:
                    hacha=0
                    print("¡Oh no, se te rompio el hacha!","\n")
                print("haz conseguido",frutosencontrados,"frutos,",palosencontrados,"palos,",hojasencontradas,"hojas y",lianasencontradas,"lianas","\n")
        elif respuesta=="alimentar fogata" and horasfogata>0:
                alimentar=int(input("¿cuantos palos quieres poner?, escribe solo el numero"))
                print("\n")
                horasfogata=horasfogata+alimentar
        elif respuesta=="comer" and frutos>0:
            print("haz comido, te sientes mejor","\n")
            frutos=frutos-1
            salud=salud+50
            while salud>saludmaxima:
                salud=salud-1
        elif respuesta=="curarse" and lianas>0 and lesion>1:
            print("cuantas lianas quieres usar del 1 al",lianas,"\n")
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
            print("estas curado","\n")
        else:
            print("no podias asi que decidiste descansar","\n")
    elif decision=="explorar":
        palosencontrados=random.randint(1,3)
        print("haz encontrado",palosencontrados,"palo/s","\n")
        piedrasencontradas=random.randint(1,3)
        print("viste",piedrasencontradas,"piedra/s","\n")
        lianasencontradas=random.randint(1,2)
        print("encontraste",lianasencontradas,"liana/s","\n")
        frutosencontrados=random.randint(1,2)
        print("haz encontrado",frutosencontrados,"fruto/s","\n")
        hojasencontradas=random.randint(2,5)
        print("encontraste",hojasencontradas,"hoja/s","\n")
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
                print("felicidades, ahora tienes una bengala","\n")
                bengala=1
        if navaja==0:
            posiblenavaja=random.randint(1,20)
            if posiblenavaja>18:
                print("perfecto, una navaja","\n")
                navaja=1
                usosnavaja==7
    else:
         print("decidiste quedarte viendo por una hora","\n")
def desafio(palos,horasjugadas,salud,saludmaxima,lanza,usoslanza,hacha,usoshacha,fogata,horasfogata,bengala,navaja,usosnavaja,lesion,efectolesion):
    enemigo=random.randint(1,5)
    if enemigo==1:
        print("oh no, te encontraste con un oso, ¿que vas a hacer?","\n","trepar","\n","correr","\n")
        if navaja==1:
            print("atacar con navaja","\n")
        if lanza==1:
            print("atacar con lanza","\n")
        if hacha==1:
            print("atacar con hacha","\n")
        if bengala==1:
            print("ahuyentar","\n")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="trepar":
            print("el oso tambien puede trepar","\n","saltas desde el arbol hacia otro y","\n")
            resultado=random.randint(1,20)
            if resultado>10:
                print("lo logras, el oso se cansa y se va","\n")
            else:
                if navaja==1 or hacha==1 or lanza==1:
                    print("te caiste, te lesionaste, pero todavia puedes defenderte, aleja al oso con","\n")
                    if navaja==1:
                        print("navaja","\n")
                    if hacha==1:
                        print("hacha","\n")
                    if lanza==1:
                        print("lanza","\n")
                    if bengala==1:
                        print("bengala")
                    respuesta=input()
                    respuesta=respuesta.lower()
                    if respuesta=="lanza" and lanza==1:
                        print("te defendiste con tu lanza","\n")
                        usoslanza=usoslanza-1
                        if usoslanza==0:
                            print("tu lanza se quebro","\n")
                            lanza=0
                    elif respuesta=="hacha" and hacha==1:
                        print("te defendiste con tu hacha","\n")
                        usoshacha=usoshacha-1
                        if usoshacha==0:
                            print("tu hacha se rompio","\n")
                            hacha=0
                    elif respuesta=="navaja" and navaja==1:
                        print("usaste la navaja para auyentar a la bestia","\n")
                        usosnavaja=usosnavaja-1
                        if usosnavaja==0:
                            print("tu navaja se rompio","\n")
                            navaja=0
                    elif respuesta=="bengala" and bengala==1:
                        print("el oso salio corriendo tras el disparo de la bengala","\n")
                        bengala=0
                    else:
                        print("tus manos estaban muy temblorosas para agarrar algo","\n")
                        salud=salud-salud
                    lesion=lesion+1
                    efectolesion=efectolesion+5
                else:
                    print("te caiste y el oso te comio vivo","\n")
                    salud=salud-salud
        elif respuesta=="correr":
            print("haz huido del oso","\n")
            resultado=random.randint(1,20)
            if resultado==20:
                print("te tropezaste en medio de la huida","\n")
                if navaja==1 or hacha==1 or lanza==1:
                    print("pero todavia puedes defenderte, aleja al oso con","\n")
                    if navaja==1:
                        print("navaja","\n")
                    if hacha==1:
                        print("hacha","\n")
                    if lanza==1:
                        print("lanza","\n")
                    respuesta==input().lower()
                    if respuesta=="lanza" and lanza==1:
                        print("te defendiste con tu lanza","\n")
                        usoslanza=usoslanza-1
                        if usoslanza==0:
                            print("tu lanza se quebro","\n")
                            lanza=0
                    elif respuesta=="hacha" and hacha==1:
                        print("te defendiste con tu hacha","\n")
                        usoshacha=usoshacha-1
                        if usoshacha==0:
                            print("tu hacha se rompio","\n")
                            hacha=0
                    elif respuesta=="navaja" and navaja==1:
                        print("usaste la navaja para auyentar a la bestia","\n")
                        usosnavaja=usosnavaja-1
                        if usosnavaja==0:
                            print("tu navaja se rompio","\n")
                            navaja=0
                    else:
                        print("no sabias que hacer y moriste devorado","\n")
                        salud=salud-salud
                else:
                    print("no pudiste hacer nada ante la embestida del oso, descansa en paz","\n")
                    salud=salud-salud
        elif respuesta=="atacar con lanza":
            print("asesinaste al oso con su lanza","\n","te curaste por completo tu salud con su carne","\n","te pusiste su piel encima")
            usoslanza=usoslanza-1
            if usoslanza==0:
                print("tu lanza se quebro","\n")
                lanza=0
            if saludmaxima<150:
             saludmaxima=saludmaxima+50
             salud=saludmaxima
        elif respuesta=="atacar con hacha":
            print("asesinaste al oso con su hacha","\n","te curaste por completo tu salud con su carne","\n","te pusiste su piel encima")
            usoshacha=usoshacha-1
            if usoshacha==0:
                print("tu hacha se quebro","\n")
                hacha=0
            if saludmaxima<150:
             saludmaxima=saludmaxima+50
             salud=saludmaxima
        elif respuesta=="atacar con navaja":
            print("asesinaste al oso con su navaja","\n","te curaste por completo tu salud con su carne","\n","te pusiste su piel encima")
            usosnavaja=usosnavaja-1
            if usosnavaja==0:
                print("tu navaja se quebro","\n")
                navaja=0
            if saludmaxima<150:
             saludmaxima=saludmaxima+50
             salud=saludmaxima
        elif respuesta=="ahuyentar":
            print("haz ahuyentado al oso exitosamente","\n")
            bengala=0
        else:
            print("te entregaste al oso, descansa en paz","\n")
            salud=salud-salud
    elif enemigo==2:
        print("ves a otro humano, pero este te empieza a atacar","\n","es un cazador, pero no esta bien de la cabeza","\n","¿que vas a hacer?","\n")
        print("huir","\n","esconderte","\n")
        if bengala==1:
            print("ahuyentarlo","\n")
        if lanza==1:
            print("arrojar lanza","\n")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="huir":
            suerte=random.randint
            if suerte>10:
                print("trataste de escapar, pero el cazador te pego un disparo a la cabeza","\n")
                salud=salud-salud
            else:
                print("escapaste con exito","\n")
        elif respuesta=="esconderse":
            print("te has escondido detras de un arbol","\n","el cazador avanza buscandote","\n","¿que haras ahora?","\n")
            print("huir lentamente","\n")
            if hacha==1:
                print("usar hacha","\n")
            if navaja==1:
                print("usar navaja","\n")
            respuesta==input()
            respuesta=respuesta.lower()
            if respuesta=="usar hacha":
                print("eliminaste la amenaza con tu hacha","\n")
                usoshacha=usoshacha-1
                if usoshacha==0:
                    print("se te ha roto el hacha","\n")
                    hacha=0
            elif respuesta=="usar navaja":
                print("eliminaste a la amenaza con tu navaja","\n")
                usosnavaja=usosnavaja-1
                if usosnavaja==0:
                    print("se te rompio la navaja","\n")
            else:
                print("haz escapado de la situacion con exito","\n")
        elif respuesta=="arrojar lanza":
            print("haz tirado tu lanza hacia su cabeza","\n")
            usoslanza=usoslanza-1
            if usoslanza==0:
                print("tu lanza se rompio tras el lanzamiento","\n")
        elif respuesta=="ahuyentarlo":
            print("haz disparado la bengala haciendo que el cazador se retire","\n")
            bengala=0
        else:
            print("haz dejado que te disparen","\n")
            salud=salud-salud
    elif enemigo==3:
        print("oh no, el arbol cobro vida","\n","¿que vas a hacer?","\n","forcejear","\n")
        if hacha==1:
            print("talar","\n")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="forcejear":
            suerte=random.randint(1,20)
            if suerte>=14:
                print("haz logrado huir con exito","\n")
            else:
                print("haz escapado, pero te has lesionado una pierna en el proceso","\n")
                lesion=lesion+1
                efectolesion=efectolesion+5
        elif respuesta=="talar" and hacha==1:
            print("haz, talado los brazos del arbol, eso fue raro","\n")
            usoshacha=usoshacha-1
            if usoshacha==0:
                print("tu hacha se ha roto","\n")
                hacha==0
        else:
            print("dejaste que el arbol hiciera lo que quisiera contigo","\n")
            lesion=lesion+1
            efectolesion==efectolesion+5
    elif enemigo==4:
        print("sientes un aullido a lo lejos","\n","es un lobo enorme","\n", "¿Que vas a hacer?","\n","intimidarlo","\n","alejarte")
        if bengala==1:
            print("ahuyentarlo","\n")
        if lanza==1:
            print("atacar con lanza","\n")
        if hacha==1:
            print("atacar con hacha","\n")
        if navaja==1:
            print("atacar con navaja","\n")
        respuesta=input()
        respuesta=respuesta.lower()
        if respuesta=="intimidarlo":
            print("haz intentado ahuyentarlo y","\n")
            suerte=random.randint(1,20)
            if suerte>=14:
                print("el lobo se fue sin atacar","\n")
            else:
                print("el lobo se enojo aun mas","\n","como saldras de esta?")
                if bengala==1:
                 print("ahuyentarlo","\n")
                if lanza==1:
                 print("atacar con lanza","\n")
                if hacha==1:
                 print("atacar con hacha","\n")
                if navaja==1:
                 print("atacar con navaja","\n")
                respuesta=input()
                respuesta=respuesta.lower()
                if respuesta=="ahuyentarlo" and bengala==1:
                    print("haz usado tu bengala para alejar al lobo","\n")
                    bengala=0
                elif respuesta=="atacar con lanza" and lanza==1:
                    print("haz usado tu lanza para atacar al lobo","\n","te pusiste tus pieles encima","\n")
                    usoslanza=usoslanza-1
                    if usoslanza==0:
                        print("tu lanza se ha roto","\n")
                        lanza=0
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                elif respuesta=="atacar con hacha" and hacha==1:
                    print("haz usado tu hacha para aniquilar al lobo","\n","haz vestido sus pieles","\n")
                    usoshacha=usoshacha-1
                    if usoshacha==0:
                        print("tu hacha se ha roto","\n")
                        hacha=0
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                elif respuesta=="atacar con navaja" and navaja==1:
                    print("haz usado tu navaja para acabar con el lobo","\n","usaste su piel para el frio","\n")
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                    usosnavaja=usosnavaja-1
                    if usosnavaja==0:
                        print("tu navaja se ha roto","\n")
                        navaja=0
                else:
                    print("te dejaste comer ante el lobo","\n")
                    salud=salud-saludmaxima
        elif respuesta=="alejarte":
            print("haz intetado escapar, pero el lobo te salto encima","\n","¿que haras al respecto?")
            if bengala==1:
                 print("ahuyentarlo","\n")
            if lanza==1:
                 print("atacar con lanza","\n")
            if hacha==1:
                 print("atacar con hacha","\n")
            if navaja==1:
                 print("atacar con navaja","\n")
            respuesta=input()
            respuesta=respuesta.lower()
            if respuesta=="ahuyentarlo" and bengala==1:
                    print("haz usado tu bengala para alejar al lobo","\n")
                    bengala=0
            elif respuesta=="atacar con lanza" and lanza==1:
                    print("haz usado tu lanza para atacar al lobo","\n","te pusiste tus pieles encima","\n")
                    usoslanza=usoslanza-1
                    if usoslanza==0:
                        print("tu lanza se ha roto","\n")
                        lanza=0
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
            elif respuesta=="atacar con hacha" and hacha==1:
                    print("haz usado tu hacha para aniquilar al lobo","\n","haz vestido sus pieles","\n")
                    usoshacha=usoshacha-1
                    if usoshacha==0:
                        print("tu hacha se ha roto","\n")
                        hacha=0
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
            elif respuesta=="atacar con navaja" and navaja==1:
                    print("haz usado tu navaja para acabar con el lobo","\n","usaste su piel para el frio","\n")
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                    usosnavaja=usosnavaja-1
                    if usosnavaja==0:
                        print("tu navaja se ha roto","\n")
                        navaja=0
            else:
                    print("te dejaste comer ante el lobo","\n")
                    salud=salud-saludmaxima        
        elif respuesta=="ahuyentarlo" and bengala==1:
                    print("haz usado tu bengala para alejar al lobo","\n")
                    bengala=0
        elif respuesta=="atacar con lanza" and lanza==1:
                    print("haz usado tu lanza para atacar al lobo","\n","te pusiste tus pieles encima","\n")
                    usoslanza=usoslanza-1
                    if usoslanza==0:
                        print("tu lanza se ha roto","\n")
                        lanza=0
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
        elif respuesta=="atacar con hacha" and hacha==1:
                    print("haz usado tu hacha para aniquilar al lobo","\n","haz vestido sus pieles","\n")
                    usoshacha=usoshacha-1
                    if usoshacha==0:
                        print("tu hacha se ha roto","\n")
                        hacha=0
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
        elif respuesta=="atacar con navaja" and navaja==1:
                    print("haz usado tu navaja para acabar con el lobo","\n","usaste su piel para el frio","\n")
                    if saludmaxima!=130 or saludmaxima!=180:
                        saludmaxima=saludmaxima+30
                    usosnavaja=usosnavaja-1
                    if usosnavaja==0:
                        print("tu navaja se ha roto","\n")
                        navaja=0
        else:
                    print("te dejaste comer ante el lobo","\n")
                    salud=salud-saludmaxima
    elif enemigo==5 and horasjugadas>=20:
        print("una ola de frio ha aparecido","\n")
        if fogata==1:
            print("te quedaste alimentando a tu fogata para que se mantenga viva un poco mas","\n","lograste que sibreviva, pero igual se redujo mucho")
            horasfogata=horasfogata-2
            palos=palos-5
            if palos<0:
                palos=0
        else:
            print("lamentablemente, no tenias como sobrevivir al frio y moriste de hipotermia","\n")
            salud=salud-saludmaxima
    else:
        print("creiste que habia pasado algo raro, pero nada mas alejado de la verdad","\n")