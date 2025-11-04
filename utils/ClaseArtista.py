class Artista:
    #-----------------ATRIBUTOS--------------------------------
    def __init__(self,nombre,edad,pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.ListaAlbumes = []

    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getPais(self):
        return self.pais
    #----------------------------------------------------------
#agregar album
    def AgregarAlbum(self,album):
        self.ListaAlbumes.append(album)
