"""Trabajo realizado por Maria Camila García Salazar - T00069283"""
from hospital import Hospital
from reportes import Reportes


def menu_principal():
    print("--------------------------------------")
    print("** GESTIÓN HOSPITALARIA SAN VICENTE **")
    print("--------------------------------------")
    print("1. Gestionar Historia Clínica Electrónica")
    print("2. Registrar Datos Médicos")
    print("3. Generar Reportes")
    print("4. Salir del Sistema")


def menu_historia_clinica():
    print("----------------------")
    print("** HISTORIA CLÍNICA **")
    print("----------------------")
    print("1. Crear Nueva Historia Clínica")
    print("2. Buscar Historia Clínica Existente")
    print("3. Dar de alta al paciente")
    print("4. Atrás")


def menu_reportes():
    print("----------------------")
    print("** GESTIÓN REPORTES **")
    print("----------------------")
    print("1. Porcentaje de Ocupación Hospitalaria")
    print("2. Promedio de Estancia por Servicio")
    print("3. Cantidad de Admisiones y Altas por Servicio")
    print("4. Pacientes con Enfermedades Crónicas")
    print("5. Prescripción de Medicamentos por Servicio")
    print("6. Atrás")


def gestion_historia_clinica(hospital):
    while True:
        menu_historia_clinica()
        opcion = input("Seleccione la opción deseada: ")
        if opcion == '1':
            hospital.crear_paciente()
        elif opcion == '2':
            id_paciente = input("Ingrese ID: ")
            paciente = hospital.buscar_paciente(id_paciente)
            if paciente:
                print("Paciente encontrado:")
                print("ID:", paciente.documento)
                print("Nombre:", paciente.nombre)
                print("Sexo:", paciente.sexo)
                print("Fecha de Nacimiento:", paciente.fecha_nacimiento)
                print("Presión Arterial:", paciente.signos_vitales.get("presion_arterial", "No disponible"))
                print("Temperatura:", paciente.signos_vitales.get("temperatura", "No disponible"))
                print("Saturación O2:", paciente.signos_vitales.get("saturacion_o2", "No disponible"))
                print("Frecuencia Respiratoria:",
                      paciente.signos_vitales.get("frecuencia_respiratoria", "No disponible"))
                print("Notas de Evolución:", paciente.notas_evolucion)
                print("Imágenes Diagnósticas:", paciente.imagenes_diagnosticas)
                print("Resultados de Exámenes de Laboratorio:", paciente.resultados_laboratorio)
                print("Medicamentos:", paciente.medicamentos)
                print("Enfermedad Crónica:", paciente.enfermedad_cronica)
            else:
                print("Paciente no encontrado.")
        elif opcion == '3':
            hospital.dar_alta_paciente()
        elif opcion == '4':
            break
        else:
            print("Opción inválida")


def gestion_reportes(hospital):
    reportes = Reportes(hospital)
    while True:
        menu_reportes()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            hospital.generar_porcentaje_ocupacion_hospitalaria()
        elif opcion == '2':
            reportes.generar_promedio_estancia_por_servicio()
        elif opcion == '3':
            reportes.generar_cantidad_admisiones_altas_por_servicio()
        elif opcion == '4':
            reportes.generar_pacientes_enfermedades_cronicas()
        elif opcion == '5':
            reportes.generar_prescripcion_medicamentos_por_servicio()
        elif opcion == '6':
            break
        else:
            print("Opción inválida")


def main():
    hospital = Hospital()
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            gestion_historia_clinica(hospital)
        elif opcion == '2':
            id_paciente = input("Ingrese ID del paciente: ")
            hospital.agregar_datos_medicos(id_paciente)
        elif opcion == '3':
            gestion_reportes(hospital)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
