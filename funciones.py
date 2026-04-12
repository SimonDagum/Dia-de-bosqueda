def ataquehacha(hacha,usoshacha):
    print(" Eliminaste al enemigo con tu hacha")
    usoshacha=usoshacha-1
    if usoshacha==0:
        print(" Haz perdido tu hacha")
        hacha=hacha-hacha
def ataquelanza(lanza,usoslanza):
    print(" Eliminaste a tus oponentes con tu lanza")
    usoslanza=usoslanza-1
    if usoslanza==0:
        print(" Te quedaste sin lanza")
        lanza=lanza-lanza
def ataquenavaja(navaja,usosnavaja):
    print(" Apuñalaste a tu adversario con la navaja")
    usosnavaja=usosnavaja-1
    if usosnavaja==0:
        print(" La navaja fue destruida en su acto heroico")
        navaja=navaja-navaja
def ahuyentar(bengala):
    print(" Aquellos que se atrevieron a atacarte se vieron asustados por tu bengala")
    bengala=bengala-bengala
def dejarsemorir (salud,saludmaxima):
    print(" Debido a tus pobres instintos de supervivencia, dejaste que el enemigo tumbara tu cuerpo")
    salud=saludmaxima
    salud=salud-saludmaxima
def pieldeoso(salud,saludmaxima):
    if saludmaxima<150:
             saludmaxima=saludmaxima+50
             salud=saludmaxima
             print(" Tu salud actual paso a subir hasta",salud)
def pieldelobo(salud,saludmaxima):
     if saludmaxima!=130 and saludmaxima!=180:
             saludmaxima=saludmaxima+30
             salud=saludmaxima
             print(" Tu salud actual paso a subir hasta",salud)
