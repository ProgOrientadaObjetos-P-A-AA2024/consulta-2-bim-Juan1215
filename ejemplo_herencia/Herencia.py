class InstitucionEducativa:
    def __init__(self, nombre, siglas):
        self.nombre = nombre
        self.siglas = siglas

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerSiglas(self, siglas):
        self.siglas = siglas

    def obtenerNombre(self):
        return self.nombre

    def obtenerSiglas(self):
        return self.siglas

class Persona:
    def __init__(self, nombre, apellido, identificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerApellido(self, apellido):
        self.apellido = apellido

    def establecerIdentificacion(self, identificacion):
        self.identificacion = identificacion

    def obtenerNombre(self):
        return self.nombre

    def obtenerApellido(self):
        return self.apellido

    def obtenerIdentificacion(self):
        return self.identificacion

class Prestamo:
    def __init__(self, beneficiario, tiempoMeses):
        self.beneficiario = beneficiario
        self.tiempoMeses = tiempoMeses
        self.ciudadPrestamo = None

    def establecerBeneficiario(self, beneficiario):
        self.beneficiario = beneficiario

    def establecerTiempoMeses(self, tiempoMeses):
        self.tiempoMeses = tiempoMeses

    def establecerCiudadPrestamo(self, ciudadPrestamo):
        self.ciudadPrestamo = ciudadPrestamo

    def obtenerBeneficiario(self):
        return self.beneficiario

    def obtenerTiempoMeses(self):
        return self.tiempoMeses

    def obtenerCiudadPrestamo(self):
        return self.ciudadPrestamo

    def __str__(self):
        cadena = (
            f"Beneficiario: {self.beneficiario.obtenerNombre()} "
            f"{self.beneficiario.obtenerApellido()}\n"
            f"Identificacion: {self.beneficiario.obtenerIdentificacion()}\n"
            f"Tiempo de prestamo: {self.tiempoMeses} meses\n"
            f"Ciudad del prestamo: {self.ciudadPrestamo}\n"
        )
        return cadena

class PrestamoAutomovil(Prestamo):
    def __init__(self, beneficiario, tiempoMeses, tipoAutomovil, marcaAutomovil, valorAutomovil):
        super().__init__(beneficiario, tiempoMeses)
        self.tipoAutomovil = tipoAutomovil
        self.marcaAutomovil = marcaAutomovil
        self.valorAutomovil = valorAutomovil
        self.valMensPrestamoAuto = 0

    def establecerTipoAutomovil(self, tipoAutomovil):
        self.tipoAutomovil = tipoAutomovil

    def establecerMarcaAutomovil(self, marcaAutomovil):
        self.marcaAutomovil = marcaAutomovil

    def establecerGaranteUno(self, garanteUno):
        self.garanteUno = garanteUno

    def establecerValorAutomovil(self, valorAutomovil):
        self.valorAutomovil = valorAutomovil

    def calcularValMensPrestamoAuto(self):
        self.valMensPrestamoAuto = self.valorAutomovil / self.tiempoMeses

    def obtenerTipoAutomovil(self):
        return self.tipoAutomovil

    def obtenerMarcaAutomovil(self):
        return self.marcaAutomovil

    def obtenerValorAutomovil(self):
        return self.valorAutomovil

    def obtenerValMensPrestamoAuto(self):
        return self.valMensPrestamoAuto

    def __str__(self):
        cadena = (
            f"{super().__str__()}"
            f"Tipo De Automovil: {self.tipoAutomovil}\n"
            f"Marca De Automovil: {self.marcaAutomovil}\n"
            f"Valor Automovil: {self.valorAutomovil:.2f}\n"
            f"Valor Mensual De Pago: {self.valMensPrestamoAuto:.2f}\n"
        )
        return cadena

class PrestamoEducativo(Prestamo):
    def __init__(self, beneficiario, tiempoMeses, nivelEstudio, institucion, valorCarrera):
        super().__init__(beneficiario, tiempoMeses)
        self.nivelEstudio = nivelEstudio
        self.institucion = institucion
        self.valorCarrera = valorCarrera
        self.valorMensual = 0

    def establecerNivelEstudio(self, nivelEstudio):
        self.nivelEstudio = nivelEstudio

    def establecerInstitucion(self, institucion):
        self.institucion = institucion

    def establecerValorCarrera(self, valorCarrera):
        self.valorCarrera = valorCarrera

    def calcularValorMensual(self):
        self.valorMensual = (self.valorCarrera / self.tiempoMeses) - (self.valorCarrera / self.tiempoMeses) * 0.10

    def obtenerNivelEstudio(self):
        return self.nivelEstudio

    def obtenerInstitucion(self):
        return self.institucion

    def obtenerValorCarrera(self):
        return self.valorCarrera

    def obtenerValorMensual(self):
        return self.valorMensual

    def __str__(self):
        cadena = (
            f"{super().__str__()}"
            f"Nivel de estudio: {self.nivelEstudio}\n"
            f"Institución educativa: {self.institucion.obtenerNombre()}\n"
            f"Institución educativa: {self.institucion.obtenerSiglas()}\n"
            f"Valor de la carrera: {self.valorCarrera:.2f}\n"
            f"Valor mensual de pago del prestamo educativo: {self.valorMensual:.2f}\n"
        )
        return cadena

import os

def mostrar_menu():
    print("Prestamos")
    print("Prestamo Automovil ingrese: 1")
    print("Prestamo Educativo ingrese: 2")
    print("Salir 3")
    return int(input())

def ingresarDatosPersona():
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    nombre = input("Nombre Del Solicitante: ")
    apellido = input("Apellido Del Solicitante: ")
    identificacion = input("Identificación Del Solicitante: ")
    return Persona(nombre, apellido, identificacion)

def ingresarDatosInstitucion():
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    nombre = input("Nombre De La Institucion: ")
    siglas = input("Siglas De La Institucion: ")
    return InstitucionEducativa(nombre, siglas)

def ingresarPrestamoAutomovil(listaPrestamos):
    tipoAutomovil = input("Tipo de automovil: ")
    marcaAutomovil = input("Marca de automovil: ")
    garante1 = ingresarDatosPersona()
    valorAutomovil = float(input("Valor de automovil: "))
    tiempoPrestamo = float(input("Tiempo de prestamo en meses: "))
    ciudadPrestamo = input("Ciudad del prestamo: ").upper()

    prestamo = PrestamoAutomovil(garante1, tiempoPrestamo, tipoAutomovil, marcaAutomovil, valorAutomovil)
    prestamo.establecerCiudadPrestamo(ciudadPrestamo)
    prestamo.calcularValMensPrestamoAuto()
    listaPrestamos.append(prestamo)

def ingresarPrestamoEducativo(listaPrestamos):
    nivelEstudio = input("Nivel de estudio: ")
    institucion = ingresarDatosInstitucion()
    valorCarrera = float(input("Valor de la carrera: "))
    tiempoPrestamo = int(input("Tiempo de prestamo en meses: "))
    ciudadPrestamo = input("Ciudad del prestamo: ").upper()
    solicitante = ingresarDatosPersona()

    prestamo = PrestamoEducativo(solicitante, tiempoPrestamo, nivelEstudio, institucion, valorCarrera)
    prestamo.establecerCiudadPrestamo(ciudadPrestamo)
    prestamo.calcularValorMensual()
    listaPrestamos.append(prestamo)

def main():
    lista_prestamos = []
    bandera = True

    while bandera:
        opc = mostrar_menu()

        if opc == 1:
            ingresarPrestamoAutomovil(lista_prestamos)
        elif opc == 2:
            ingresarPrestamoEducativo(lista_prestamos)
        elif opc == 3:
            bandera = False
        else:
            print("Solo opciones 1 y 2")

        salida = input("\nIngrese 'si' si desea salir del Sistema: ")
        if salida.lower() == "si":
            bandera = False

    print("\nLista de prestamos registrados:\n")
    for prestamo in lista_prestamos:
        print(prestamo)

if __name__ == "__main__":
    main()
