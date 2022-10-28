class NotaEstudiante():
    def __init__(self,idNota,calificacion,fecha):
        self.idNota=idNota
        self.calificacion=calificacion
        self.fecha=fecha

    def mostrarNota(self):
        return "\nId Nota  : "+str(self.idNota)+\
                "\nCalificacion  : "+self.calificacion+\
                "\nFecha  : "+self.fecha.MostrarFecha()

                
                