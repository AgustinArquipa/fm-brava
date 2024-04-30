from django.db import models

# Create your models here.
class Program(models.Model):
    # Nombre del programa y descripcion del programa
    name = models.CharField(
        max_length=100,
        verbose_name="Nombre del Programa",
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descripcion del Programa"
    )
    # Fecha y hora de comienzo del programa
    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha"
    )
    start_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Hora Inicio"
    )
    end_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Hora Fin"
    )
    # Locutor a cargo del programa

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"
        db_table = "Programs"

    def __str__(self) -> str:
        return f"Programa: {self.name} - {str(self.date.strftime('%d-%m-%Y'))}:{str(self.start_time.strftime('%H:%M'))}"