#################### EJERCICIO 07 ############################
# Un ciclista parte de la Plaza del Pilar de Zaragoza en ruta hasta la Plaza Navarra de Huesca. 
# Ambos puntos están separados por 76 km y el ciclista los recorre a una velocidad de 30 km/h.
# Calcula a qué hora, minutos y segundos llegará el ciclista a Huesca si se le proporciona al script 
# mediante la entrada estándar la hora, minuto y segundos en las que saldrá de Zaragoza.
# El script deberá verificar que no se introducen o generan valores horarios incoherentes. 
# Para facilitar la tarea se considerará que el ciclista no puede partir de Zaragoza antes de las 8:00:00 
# y después de las 18:00:00 ya que quiere realizar el recorrido completo con luz natural.

distance = 76
speed = 30

hour_depart = int(input("Hora de salida: "))
min_depart = int(input("Minuto de salida: "))
sec_depart = int(input("Segundos de salida: "))

if hour_depart > 17 or hour_depart < 8 or min_depart < 0 or min_depart > 59 or sec_depart < 0 or sec_depart > 59:
    print("Hora incorrecta")
    exit()

# Segundos que tarda en ir Zgz a Hu
sec_travel = (distance / speed) * 3600

# Segundos con los que se inicia el viaje
sec_initial = hour_depart * 3600 + min_depart * 60 + sec_depart

# Referencia de tiempo de llegada
sec_final = sec_initial + sec_travel

# Conversión a horas, minutos y segundos
hour_arrival = int(sec_final // 3600)
min_arrival = int((sec_final % 3600) // 60)
sec_arrival = int((sec_final % 3600) % 60)

print(hour_arrival,":",min_arrival,":",sec_arrival)