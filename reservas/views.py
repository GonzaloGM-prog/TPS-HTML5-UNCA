from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import ActividadDeportiva

# Cupo máximo permitido al registrar una actividad (se puede ajustar).
CUPO_MAXIMO = 1000


def hola_mundo(request):
    return render(request, "reservs/hola.html")


def index(request):
    return render(request, "reservs/index.html")


def validar_actividad(datos):
    """Valida los datos del formulario y devuelve la lista de errores.

    Si la lista está vacía, los datos son correctos.
    """
    errores = []

    if not datos["nombre"]:
        errores.append("El nombre es obligatorio.")
    elif len(datos["nombre"]) > 100:
        errores.append("El nombre no puede superar los 100 caracteres.")

    if not datos["descripcion"]:
        errores.append("La descripción es obligatoria.")

    if not datos["lugar"]:
        errores.append("El lugar es obligatorio.")
    elif len(datos["lugar"]) > 100:
        errores.append("El lugar no puede superar los 100 caracteres.")

    try:
        cupo = int(datos["cupo"])
    except ValueError:
        errores.append("El cupo debe ser un número entero.")
    else:
        if cupo < 1:
            errores.append("El cupo debe ser al menos 1.")
        elif cupo > CUPO_MAXIMO:
            errores.append(f"El cupo no puede superar {CUPO_MAXIMO} participantes.")

    return errores


def agregar_actividad(request):
    """Muestra el formulario de alta y, al enviarlo por POST, guarda la actividad."""
    datos = {"nombre": "", "descripcion": "", "lugar": "", "cupo": ""}

    if request.method == "POST":
        datos = {campo: request.POST.get(campo, "").strip() for campo in datos}
        errores = validar_actividad(datos)

        if errores:
            for error in errores:
                messages.error(request, error)
        else:
            actividad = ActividadDeportiva.objects.create(
                nombre=datos["nombre"],
                descripcion=datos["descripcion"],
                lugar=datos["lugar"],
                cupo=int(datos["cupo"]),
            )
            messages.success(
                request, f"La actividad «{actividad.nombre}» se registró correctamente."
            )
           
            return redirect("agregar_actividad")

    return render(request, "reservas/agregar_actividad.html", {"datos": datos})


def lista_actividades(request):
    """Muestra todas las actividades deportivas registradas."""
    actividades = ActividadDeportiva.objects.all()
    return render(
        request, "reservas/lista_actividades.html", {"actividades": actividades}
    )


def detalle_actividad(request, actividad_id):
    """Muestra los datos completos de una actividad (404 si no existe)."""
    actividad = get_object_or_404(ActividadDeportiva, pk=actividad_id)
    horarios = actividad.horarios.all()
    return render(
        request,
        "reservas/detalle_actividad.html",
        {"actividad": actividad, "horarios": horarios},
    )