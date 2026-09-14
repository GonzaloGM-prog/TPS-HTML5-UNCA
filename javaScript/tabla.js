const actividades = [
    {
        actividad: "Fútbol",
        lugar: "Polideportivo UNCA",
        dia: "Lunes",
        horario: "18:00 - 20:00",
        cupos: 20,
        estado: "Disponible"
    },
    {
        actividad: "Básquet",
        lugar: "Gimnasio UNCA",
        dia: "Martes",
        horario: "16:00 - 18:00",
        cupos: 15,
        estado: "Disponible"
    },
    {
        actividad: "Vóley",
        lugar: "Polideportivo UNCA",
        dia: "Miércoles",
        horario: "18:00 - 20:00",
        cupos: 12,
        estado: "Completo"
    },
    {
        actividad: "Atletismo",
        lugar: "Pista de Atletismo",
        dia: "Jueves",
        horario: "17:00 - 19:00",
        cupos: 25,
        estado: "Disponible"
    }
];

const tablaActividades = document.getElementById("tablaActividades");
const cuerpoTabla = document.getElementById("cuerpoTabla");

if (tablaActividades && cuerpoTabla) {
    actividades.forEach((act) => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <td>${act.actividad}</td>
            <td>${act.lugar}</td>
            <td>${act.dia}</td>
            <td>${act.horario}</td>
            <td>${act.cupos}</td>
            <td>${act.estado}</td>
        `;
        cuerpoTabla.appendChild(fila);
    });
}

const cantidadParticipantes = document.getElementById("cantidadParticipantes");
const generarParticipantes = document.getElementById("generarParticipantes");
const contenedorParticipantes = document.getElementById("contenedorParticipantes");

if (cantidadParticipantes && generarParticipantes && contenedorParticipantes) {
    generarParticipantes.addEventListener("click", () => {
        const cantidad = Number(cantidadParticipantes.value);

        if (!Number.isInteger(cantidad) || cantidad < 1 || cantidad > 10) {
            alert("Ingrese una cantidad de participantes entre 1 y 10.");
            return;
        }

        const tabla = document.createElement("table");
        tabla.innerHTML = `
            <thead>
                <tr>
                    <th>#</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>DNI</th>
                </tr>
            </thead>
            <tbody></tbody>
        `;

        const cuerpoParticipantes = tabla.querySelector("tbody");

        for (let indice = 1; indice <= cantidad; indice += 1) {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${indice}</td>
                <td><input type="text" name="participantes[${indice}][nombre]" aria-label="Nombre del participante ${indice}" required></td>
                <td><input type="text" name="participantes[${indice}][apellido]" aria-label="Apellido del participante ${indice}" required></td>
                <td><input type="text" name="participantes[${indice}][dni]" inputmode="numeric" pattern="[0-9]{8}" aria-label="DNI del participante ${indice}" required></td>
            `;
            cuerpoParticipantes.appendChild(fila);
        }

        contenedorParticipantes.replaceChildren(tabla);
    });
}