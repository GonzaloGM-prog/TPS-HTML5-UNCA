function validarFechaNacimiento(fechaIngresada) {
    const fechaNac = new Date(fechaIngresada);
    const fechaActual = new Date();

    if (!fechaIngresada || Number.isNaN(fechaNac.getTime())) {
        alert("Ingrese una fecha válida");
        return false;
    }

    if (fechaNac > fechaActual) {
        alert("La fecha de nacimiento no puede ser posterior a la fecha actual");
        return false;
    }

    if (fechaNac.getFullYear() < 1900) {
        alert("La fecha de nacimiento debe ser mayor a 1900");
        return false;
    }

    return true;
}

function validarDNI(dni) {
    const regexDNI = /^\d{8}$/;

    if (!regexDNI.test(dni)) {
        alert("El DNI debe contener 8 dígitos");
        return false;
    }

    return true;
}

const formulario = document.querySelector("form");
const fechaNacimientoInput = document.getElementById("fechaNacimiento");
const dniInput = document.getElementById("dni");

if (formulario && fechaNacimientoInput && dniInput) {
    formulario.addEventListener("submit", function(event) {
        const fecha = fechaNacimientoInput.value;
        const dni = dniInput.value;

        if (!validarFechaNacimiento(fecha) || !validarDNI(dni)) {
            event.preventDefault();
        }
    });
}