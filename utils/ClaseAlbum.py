#ÁLBUM

#Tiene:
#Nombre
#Portada
#Tracklist
#Duración

class Album: #Hereda artista de Artista
    
    #------------------------------------------ATRIBUTOS
    def __init__(self,tracklist,año,portada,duracion):
        self.tracklist = tracklist
        self.año = año
        self.portada = portada
        self.duracion = duracion
    
    #------------------------------------------GETS
    def getTracklist(self):
        return self.tracklist
    
    def getAño(self):
        return self.año
    
    def getPortada(self):
        return self.portada
    
    def getDuracion(self):
        return self.duracion
    
    #------------------------------------------ Metodos
    
    def añadirCancion(self,cancion):
        self.tracklist.append(cancion)
        return True
    
    def quitarCancion(self,titulo):
        if self.tracklist.count(titulo) > 0:
            self.tracklist.pop(titulo)
            return True
        else:
            return False
    
    def cambiarPortada(self,portada):
        self.portada = portada
        return True