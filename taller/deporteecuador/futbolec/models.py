from django.db import models

# Create your models here.

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=50)

    def __str__(self):
        return "Nombre: %s - Siglas: %s - Twitter: %s" % (
            self.nombre,
            self.siglas,
            self.username_twitter 
        )


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)

    def __str__(self):
        return "Nombre: %s - Posición: %s - Camiseta: %d - Sueldo: %.2f - Equipo: %s" % (
            self.nombre,
            self.posicion_campo,
            self.numero_camiseta,
            self.sueldo,
            self.equipo.nombre
        )


class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return "Campeonato: %s - Auspiciante: %s" % (
            self.nombre_campeonato,
            self.auspiciante
        )


class CampeonatoEquipo(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return "Año: %d - Equipo: %s - Campeonato: %s (Auspiciante: %s)" % (
            self.anio,
            self.equipo.nombre,
            self.campeonato.nombre_campeonato,
            self.campeonato.auspiciante
        )
