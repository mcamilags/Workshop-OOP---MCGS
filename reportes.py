from datetime import datetime
from hospital import calcular_estancia


class Reportes:
    def __init__(self, hospital):
        self.hospital = hospital

    def generar_promedio_estancia_por_servicio(self):
        fecha_fin = input("Ingrese la fecha de fin para el informe (DD/MM/AAAA): ")
        print("Fecha:", datetime.now().strftime("%d/%m/%Y"))
        print("Fecha de fin del informe:", fecha_fin)

        print("Servicios disponibles:")
        for i, servicio in enumerate(self.hospital.servicios, 1):
            print(f"{i}. {servicio}")
        servicio_elegido = int(input("Seleccione el número del servicio para el informe: "))
        servicio_seleccionado = self.hospital.servicios[servicio_elegido - 1]

        pacientes_servicio = [paciente for paciente in self.hospital.pacientes if
                              servicio_seleccionado.lower() in paciente.servicio.lower()]
        pacientes_dados_de_alta = [paciente for paciente in pacientes_servicio if paciente.fecha_alta]

        if pacientes_dados_de_alta:
            estancias = []
            for paciente in pacientes_dados_de_alta:
                if paciente.fecha_alta <= fecha_fin:
                    estancia = calcular_estancia(paciente.fecha_ingreso, paciente.fecha_alta, paciente.fecha_ingreso,
                                                 fecha_fin)
                else:
                    estancia = calcular_estancia(paciente.fecha_ingreso, fecha_fin, paciente.fecha_ingreso, fecha_fin)
                estancias.append(estancia)

            if estancias:
                promedio_estancia = sum(estancias) / len(estancias)
                print("Promedio de Estancia para el Servicio {}:".format(servicio_seleccionado))
                print("Promedio de Estancia:", round(promedio_estancia, 2), "días")
            else:
                print("No hay pacientes en el servicio {} con fecha de alta antes de {}.".format(servicio_seleccionado,
                                                                                                 fecha_fin))
        else:
            print("No se encontraron pacientes dados de alta en el servicio {}.".format(servicio_seleccionado))

    def generar_prescripcion_medicamentos_por_servicio(self):

        print("Servicios disponibles:")
        for i, servicio in enumerate(self.hospital.servicios, 1):
            print(f"{i}. {servicio}")
        servicio_elegido = int(
            input("Seleccione el número del servicio para el informe de prescripción de medicamentos: "))
        servicio_seleccionado = self.hospital.servicios[servicio_elegido - 1]

        pacientes_servicio = [paciente for paciente in self.hospital.pacientes if
                              servicio_seleccionado.lower() in paciente.servicio.lower()]
        if pacientes_servicio:
            print("Prescripción de Medicamentos para el Servicio {}:".format(servicio_seleccionado))
            for paciente in pacientes_servicio:
                print("- Paciente: {}, Medicamentos: {}".format(paciente.nombre, ", ".join(paciente.medicamentos)))
        else:
            print("No se encontraron pacientes en el servicio especificado.")

    def generar_cantidad_admisiones_altas_por_servicio(self):
        for servicio in self.hospital.servicios:
            pacientes_servicio = [paciente for paciente in self.hospital.pacientes if
                                  servicio.lower() in paciente.servicio.lower()]
            admisiones = sum(1 for paciente in pacientes_servicio if not paciente.fecha_alta)
            altas = sum(1 for paciente in pacientes_servicio if paciente.fecha_alta)
            print("Informe de Admisiones y Altas para el Servicio {}:".format(servicio))
            print("Fecha:", datetime.now().strftime("%d/%m/%Y"))
            print("- Admisiones:", admisiones)
            print("- Altas:", altas)

    def generar_pacientes_enfermedades_cronicas(self):
        pacientes_cronicos = [paciente for paciente in self.hospital.pacientes if paciente.enfermedad_cronica]
        if pacientes_cronicos:
            print("Pacientes con Enfermedades Crónicas:")
            for paciente in pacientes_cronicos:
                print("- Nombre: {}, ID: {}, Enfermedad: {}".format(paciente.nombre, paciente.documento,
                                                                    paciente.enfermedad_cronica))
        else:
            print("No hay pacientes con enfermedades crónicas registradas.")
