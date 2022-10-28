
from docente import Docente
from estudiante import Estudiante
from nota import NotaEstudiante
from dia    import Fecha
listaDocentes=[]
listaEstudiantes=[]

f=Fecha(21,12,2001)
#print(f.MostrarFecha())
n=NotaEstudiante(2,'4.5',f)
#print(n.mostrarNota())

e=Estudiante(2,'alonso','1B',n)
#print(e.MostrarEstudiante())
listaEstudiantes.append(e)
d=Docente(1,'javier','Programacion',e)
listaDocentes.append(d)
d=Docente(2,'jv','Programacion',e) 
listaDocentes.append(d)
d=Docente(3,'jas','Programacion',e) 
#print(d.MostrarDocente())
listaDocentes.append(d)
#e.MostrarEstudiante()
#for y in listaDocentes:
    #print('lista docente -----',y.MostrarDocente())
#for f in listaEstudiantes:
    #print('lista Estudiantes  ---',f.MostrarEstudiante())

while True:
    print('---------OPCION 1: AGREGAR DOCENTE---------')
    print('---------OPCION 2: agregarEstudiante---------')
    print('---------OPCION 3: modificarNota---------')
    print('---------OPCION 4: modificarNota---------')
    op=int(input('ingrese opcion : -------'))
    if op==1:
        d.MostrarListaDocente(listaDocentes)
        idNuevo=int(input('ingrese el id  : -------'))
        d.AgregarDocente(idNuevo,listaDocentes)
        


    elif op==2:
        print('Lista de Docentes, presione 1')
        print('Lista de Estudiantes, presione 2')
        opc=input('Desea ver lista de estudiantes o de docentes')
        if opc==1:
            for Doc in listaDocentes:
                print(Doc.MostrarDocente(listaDocentes))
    