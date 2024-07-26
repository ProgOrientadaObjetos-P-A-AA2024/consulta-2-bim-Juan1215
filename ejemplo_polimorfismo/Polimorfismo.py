from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, caracteristicas):
        self.caracteristicas = caracteristicas
        self.area = 0

    def establecer_caracteristicas(self, caracteristicas):
        self.caracteristicas = caracteristicas

    @abstractmethod
    def calcular_area(self):
        pass

    def obtener_caracteristicas(self):
        return self.caracteristicas

    def obtener_area(self):
        return self.area

    def __str__(self):
        return f"Caracteristicas: {self.caracteristicas}\nÁrea: {self.area:.2f}"

class Cuadrado(Figura):
    def __init__(self, caracteristicas, lado):
        super().__init__(caracteristicas)
        self.lado = lado

    def establecer_lado(self, lado):
        self.lado = lado

    def calcular_area(self):
        self.area = self.lado ** 2

    def obtener_lado(self):
        return self.lado

    def __str__(self):
        return f"{super().__str__()}\nLado: {self.lado:.2f}"

class Rombo(Figura):
    def __init__(self, caracteristicas, diagonal_menor, diagonal_mayor):
        super().__init__(caracteristicas)
        self.diagonal_menor = diagonal_menor
        self.diagonal_mayor = diagonal_mayor

    def establecer_diagonal_menor(self, diagonal_menor):
        self.diagonal_menor = diagonal_menor

    def establecer_diagonal_mayor(self, diagonal_mayor):
        self.diagonal_mayor = diagonal_mayor

    def calcular_area(self):
        self.area = (self.diagonal_menor * self.diagonal_mayor) / 2

    def obtener_diagonal_menor(self):
        return self.diagonal_menor

    def obtener_diagonal_mayor(self):
        return self.diagonal_mayor

    def __str__(self):
        return (f"{super().__str__()}\nDiagonal Menor: {self.diagonal_menor:.2f}\n"
                f"Diagonal Mayor: {self.diagonal_mayor:.2f}")

class Triangulo(Figura):
    def __init__(self, caracteristicas, base, altura):
        super().__init__(caracteristicas)
        self.base = base
        self.altura = altura

    def establecer_base(self, base):
        self.base = base

    def establecer_altura(self, altura):
        self.altura = altura

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def obtener_base(self):
        return self.base

    def obtener_altura(self):
        return self.altura

    def __str__(self):
        return f"{super().__str__()}\nBase: {self.base:.2f}\nAltura: {self.altura:.2f}"

class Ejecutor:
    @staticmethod
    def main():
        figuras = []

        print("Áreas Registradas de Cuadrado\n")
        caracteristica = input("Característica de la Figura: ")
        for i in range(4):
            lado = float(input(f"Ingrese lado del Cuadrado {i + 1} (cm): "))
            print("--------------------------------------------")
            cuadrado = Cuadrado(caracteristica, lado)
            cuadrado.calcular_area()
            figuras.append(cuadrado)

        print("\nÁreas Registradas de Rombo\n")
        caracteristica = input("Característica de la Figura: ")
        for i in range(3):
            diagonal_mayor = float(input("Diagonal Mayor del Rombo (cm): "))
            diagonal_menor = float(input("Diagonal Menor del Rombo (cm): "))
            print("--------------------------------------------")
            rombo = Rombo(caracteristica, diagonal_menor, diagonal_mayor)
            rombo.calcular_area()
            figuras.append(rombo)

        print("\nÁreas Registradas de Triángulo\n")
        caracteristica = input("Característica de la Figura: ")
        for i in range(5):
            base = float(input("Base del Triángulo (cm): "))
            altura = float(input("Altura del Triángulo (cm): "))
            print("--------------------------------------------")
            triangulo = Triangulo(caracteristica, base, altura)
            triangulo.calcular_area()
            figuras.append(triangulo)

        print("\nDatos de Figuras\n")
        for figura in figuras:
            figura.calcular_area()
            print(figura)

if __name__ == "__main__":
    Ejecutor.main()
