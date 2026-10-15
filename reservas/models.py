from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class ActividadDeportiva(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=100)
    cupo = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Actividad deportiva"
        verbose_name_plural = "Actividades deportivas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    DIAS = [
        ("LUN", "Lunes"),
        ("MAR", "Martes"),
        ("MIE", "Miércoles"),
        ("JUE", "Jueves"),
        ("VIE", "Viernes"),
        ("SAB", "Sábado"),
        ("DOM", "Domingo"),
    ]

    actividad = models.ForeignKey(
        ActividadDeportiva,
        on_delete=models.CASCADE,
        related_name="horarios",
    )
    dia = models.CharField(max_length=3, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        ordering = ["actividad", "dia", "hora_inicio"]

    def clean(self):
        if self.hora_inicio and self.hora_fin and self.hora_fin <= self.hora_inicio:
            raise ValidationError("La hora de fin debe ser posterior a la hora de inicio.")

    def __str__(self):
        return f"{self.actividad.nombre} - {self.get_dia_display()} {self.hora_inicio:%H:%M}-{self.hora_fin:%H:%M}"

class Inscripcion(models.Model):
    ACTIVA = "ACTIVA"
    CANCELADA = "CANCELADA"
    ESTADOS = [
        (ACTIVA, "Activa"),
        (CANCELADA, "Cancelada"),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default=ACTIVA)
    horario = models.ForeignKey(
        Horario,
        on_delete=models.CASCADE,
        related_name="inscripciones",
    )

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        ordering = ["-fecha_inscripcion"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI {self.dni}) - {self.get_estado_display()}"