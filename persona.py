class Persona:
    def __init__(self, nombre: str = "john", apellido: str = "doe", du: int = 12345678):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__du__ = du

    def atributos(self):
        print(f"Mis datos son: Nombre: {self.__nombre__}, Apellido: {self.__apellido__}, DU: {self.__du__}")

    def __str__(self):
        return f"Mis datos son: Nombre: {self.__nombre__}, Apellido: {self.__apellido__}, DU: {self.__du__}"