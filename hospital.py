from datetime import datetime


class Paciente:
    def __init__(self, documento, nombre, sexo, fecha_nacimiento):
        self.documento = documento
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.signos_vitales = {}
        self.notas_evolucion = ""
        self.imagenes_diagnosticas = []
        self.resultados_laboratorio = ""
        self.medicamentos = []
        self.enfermedad_cronica = None
        self.fecha_ingreso = None
        self.fecha_alta = None
        self.servicio = ""

    def agregar_signos_vitales(self, presion_arterial, temperatura, saturacion_o2, frecuencia_respiratoria):
        self.signos_vitales = {
            "presion_arterial": presion_arterial,
            "temperatura": temperatura,
            "saturacion_o2": saturacion_o2,
            "frecuencia_respiratoria": frecuencia_respiratoria
        }

    def agregar_nota_evolucion(self, notas):
        self.notas_evolucion = notas

    def agregar_imagen_diagnostica(self, imagen):
        self.imagenes_diagnosticas.append(imagen)

    def agregar_resultados_laboratorio(self, resultados):
        self.resultados_laboratorio = resultados

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)


def calcular_estancia(fecha_ingreso, fecha_alta, fecha_inicio, fecha_fin):
    fecha_inicio = parse_fecha(fecha_inicio)
    fecha_fin = parse_fecha(fecha_fin)
    if fecha_ingreso:
        fecha_ingreso = parse_fecha(fecha_ingreso)
    if fecha_alta:
        fecha_alta = parse_fecha(fecha_alta)

    if fecha_ingreso and fecha_inicio <= fecha_ingreso <= fecha_fin:
        if fecha_alta:
            if fecha_ingreso < fecha_inicio:
                fecha_ingreso = fecha_inicio
            if fecha_alta > fecha_fin:
                fecha_alta = fecha_fin
            return (fecha_alta - fecha_ingreso).days
    return 0


def parse_fecha(fecha_str):
    partes = fecha_str.split('/')
    if len(partes) != 3:
        raise ValueError("El formato de fecha debe ser DD/MM/AAAA")
    dia, mes, anio = partes
    return datetime(int(anio), int(mes), int(dia))


class Hospital:
    def __init__(self):
        self.pacientes = []
        self.capacidad_total = 300
        self.servicios = ["Cardiología", "Consulta general", "Traumatología", "Ginecología", "Neurología", "Pediatría",
                          "Oncología", "Endocrinología", "Nefrología", "Gastroenterología", "Dermatología"]

    def crear_paciente(self):
        documento = input("Ingrese el documento del paciente: ")
        nombre = input("Ingrese el nombre del paciente: ")
        sexo = input("Ingrese el sexo del paciente (M/F): ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (DD/MM/AAAA): ")
        fecha_ingreso = input("Ingrese la fecha de ingreso del paciente (DD/MM/AAAA): ")

        paciente = Paciente(documento, nombre, sexo, fecha_nacimiento)
        paciente.fecha_ingreso = fecha_ingreso
        print("Servicios disponibles:")
        for i, servicio in enumerate(self.servicios, 1):
            print(f"{i}. {servicio}")
        servicio_elegido = int(input("Seleccione el número del servicio del paciente: "))
        paciente.servicio = self.servicios[servicio_elegido - 1]

        self.pacientes.append(paciente)
        print("¡Paciente agregado con éxito!")
        return paciente

    def agregar_datos_medicos(self, id_paciente):
        paciente = self.buscar_paciente(id_paciente)
        if paciente:
            presion_arterial = input("Ingrese la presión arterial del paciente: ")
            temperatura = input("Ingrese la temperatura del paciente: ")
            saturacion_o2 = input("Ingrese la saturación de oxígeno del paciente: ")
            frecuencia_respiratoria = input("Ingrese la frecuencia respiratoria del paciente: ")

            paciente.agregar_signos_vitales(presion_arterial, temperatura, saturacion_o2, frecuencia_respiratoria)

            notas = input("Ingrese las notas de evolución del paciente: ")
            paciente.agregar_nota_evolucion(notas)

            imagen = input("Ingrese la ruta de la imagen diagnóstica del paciente: ")
            paciente.agregar_imagen_diagnostica(imagen)

            resultados = input("Ingrese los resultados de los exámenes de laboratorio del paciente: ")
            paciente.agregar_resultados_laboratorio(resultados)

            medicamento = input("Ingrese el medicamento prescrito al paciente: ")
            paciente.agregar_medicamento(medicamento)

            enfermedad_cronica = input("Es una enfermedad crónica (s/n): ")
            if enfermedad_cronica.lower() == 's':
                nombre_enfermedad = input("Nombre de la enfermedad: ")
                paciente.enfermedad_cronica = nombre_enfermedad
        else:
            print("¡Paciente no encontrado!")

    def dar_alta_paciente(self):
        id_paciente = input("Ingrese el ID del paciente a dar de alta: ")
        paciente = self.buscar_paciente(id_paciente)
        if paciente:
            fecha_alta = input("Ingrese la fecha de alta del paciente (DD/MM/AAAA): ")
            paciente.fecha_alta = fecha_alta
            print("¡Paciente dado de alta correctamente!")
        else:
            print("¡No existe paciente con ese ID!")

    def generar_porcentaje_ocupacion_hospitalaria(self):
        camas_ocupadas = sum(1 for paciente in self.pacientes if not paciente.fecha_alta)
        porcentaje_ocupacion = (camas_ocupadas / self.capacidad_total) * 100
        print("Porcentaje de Ocupación Hospitalaria:")
        print("Fecha:", datetime.now().strftime("%d/%m/%Y"))
        print("Porcentaje de Ocupación:", round(porcentaje_ocupacion, 2), "%")
        print("Camas Ocupadas:", camas_ocupadas)
        print("Camas Disponibles:", self.capacidad_total - camas_ocupadas)

    def buscar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.documento == id_paciente:
                return paciente
        return None
