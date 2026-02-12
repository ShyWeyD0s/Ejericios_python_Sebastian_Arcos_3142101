#Creamos la tres listas para cada equipo, estas de 3 elementos
BasicsFtbll=[0, 0, 0]
CasiusNac=[0, 0, 0]
RapidFire=[0, 0, 0]
#Introducimos datos de Equipo RapidFire
RapidFire[0] = int(input("Introduzca la cantidad de partidos ganados del RapidFire: "))
RapidFire[1] = int(input("Introduzca la cantidad de partidos empatados del RapidFire: "))
RapidFire[2] = int(input("Introduzca la cantidad de partidos perdidos del RapidFire: "))
#Introducimos datos de equipo CasiusNac
CasiusNac[0] = int(input("Introduzca la cantidad de partidos ganados del CasiusNac: "))
CasiusNac[1] = int(input("Introduzca la cantidad de partidos empatados del CasiusNac: "))
CasiusNac[2] = int(input("Introduzca la cantidad de partidos perdidos del CasiusNac: "))
#Introducimos datos de Equipo BasicsFtbll
BasicsFtbll[0] = int(input("Introduzca la cantidad de partidos ganados del equipo BasicsFtbll: "))
BasicsFtbll[1] = int(input("Introduzca la cantidad de partidos empatados del equipo BasicsFtbll: "))
BasicsFtbll[2] = int(input("Introduzca la cantidad de partidos perdidos del equipo BasicsFtbll: "))
#Imprimimos los datos
print(
    "la cantidad de partidos ganados del equipo CasiusNac: ", CasiusNac[0],
    "la cantidad de partidos empatados del equipo CasiusNac:", CasiusNac[1],
    "la cantidad de partidos perdidos del equipo CasiusNac: ", CasiusNac[2], )

print(
    "La cantidad de partidos ganados del equipo RapidFire:", RapidFire[0],
    "la cantidad de partidos empatados del equipo RapidFire:", RapidFire[1],
    "la cantidad de partidos perdidos del equipo RapidFire:", RapidFire[2],)

print(
    "La cantidad de partidos ganados del equipo BasicsFtbll:", BasicsFtbll[0],
    "la cantidad de partidos empatados del equipo BasicsFtbll:", BasicsFtbll[1],
    "la cantidad de partidos perdidos del equipo BasicsFtbll:", BasicsFtbll[2])
#operaciones para calcular  el puntaje total
puntajeCasius = CasiusNac[0] * 3
puntajeBasics = BasicsFtbll[0] * 3
puntajeRapid = RapidFire[0] * 3
totalCasius = "CasiusNac: ", puntajeCasius + CasiusNac[1]
totalBasics= "BasicsFtbll ", puntajeBasics + BasicsFtbll[1]
totalRapid = "RapidFire: ", puntajeRapid + RapidFire[1]

#Imprimimos la tabla de clasificacion en orden de puntaje
tablaClasi = [totalRapid, totalBasics, totalCasius]
print("La tabla de puntos Clasificada por abecedario:", sorted(tablaClasi))