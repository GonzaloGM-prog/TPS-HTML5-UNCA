function Actividad(nombre, lugar, dia, horario, cupo, estado) {
    this.nombre = nombre;
    this.lugar = lugar;
    this.dia = dia;
    this.horario = horario;
    this.cupo = cupo;
    this.estado = estado; 
}
class SistemaDeportes{
    constructor(){
        this.actividades = [];
    }
    agregarActividad(nombre, lugar, dia, horario, cupo, estado){
        this.actividades.push(new Actividad(nombre, lugar, dia, horario, cupo, estado));
    }
    listarActividades() {
        console.log("--- Lista de Actividades Deportivas ---");
        this.actividades.forEach((act, index) => {
            console.log(`${index + 1}. ${act.nombre} - Lugar: ${act.lugar} | Día: ${act.dia} | Horario: ${act.horario} | Cupo: ${act.cupo} | Estado: ${act.estado}`);
        });
    }
}
const sistema = new SistemaDeportes();
sistema.agregarActividad("Fútbol", "Campo de fútbol", "Martes", "10:00", 25, "Disponible");
sistema.agregarActividad("Básquet", "Pista", "Martes", "10:00", 25, "Disponible");
sistema.agregarActividad("Vóley", "Pista", "Martes", "10:00", 25, "Disponible");
sistema.agregarActividad("Atletismo", "Pista", "Martes", "10:00", 25, "Disponible");
sistema.listarActividades();