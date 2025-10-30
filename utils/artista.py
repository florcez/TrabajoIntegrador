class artista:
    #-----------------ATRIBUTOS--------------------------------
    def __init__(self,imagen,nombre,nacimiento,pais):
        self.imagen = imagen
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.pais = pais
        self.ListaAlbumes = []


    def getImagen(self):
        return self.imagen
    def getNombre(self):
        return self.nombre
    def getNacimiento(self):
        return self.nacimiento
    def getPais(self):
        return self.pais
    #----------------------------------------------------------


#agregar album
    def AgregarAlbum(self,album):
        self.ListaAlbumes.append(album)
